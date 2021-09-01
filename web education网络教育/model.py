import view
import sql
import traceback
from bottle import request, response 
from decoraters import require_logged_in, secured

# Initialise our views, all arguments are defaults for the template
page_view = view.View()
sql_db = sql.SQLDatabase("w4school.db")



##############################################################################
##################################  Login  ###################################
##############################################################################
def login_form():

    session = request.get_cookie("SESSIONID")
    if not sql_db.session_is_expire(session):
        return page_view("course")
    return page_view("login")


def log_out():

    response.delete_cookie(name="SESSIONID")

    return page_view("logout")


def login_check(email, password):

    if not email.strip() or not password.strip():
        return "<script> alert('empty email or password') </script>"
    login = sql_db.check_credentials(email, password)
    if login:
        SESSIONID,ExpireTime = sql_db.create_session(email, request.remote_addr)
        response.set_cookie(name="SESSIONID", value=SESSIONID, expires=ExpireTime, secure=True)

        return page_view("valid", name=email)
    else:
        return page_view("invalid")



##############################################################################
#################################  Sign Up  ##################################
##############################################################################


def sign_up_form():

    return page_view("signup")


@secured()
def sign_up(email, password, displayname, question, answer):

    if  not email or not password or \
        not displayname or not question or not answer:
        return "<script> alert(\"Empty Email or Password!\");</script>"

    try:
        signup = sql_db.add_user(email, password, displayname)
        safety = sql_db.set_safety(email, question, answer)
        
        if signup and safety: 
            return page_view("signup_success")
        else:
            return page_view("signup_fail")
    except:
        return """
            <center>
            <p>Email exists!</p>
            <a href="/signup">try again</a>
            </center>
        """



##############################################################################
###################################  Feeds  ##################################
##############################################################################
@require_logged_in(sql_db)
def feed(userid):

    return page_view("feed")



##############################################################################
###########################  Account and Settings  ###########################
##############################################################################
@require_logged_in(sql_db)
def account(userid):
    """
        account
        Returns the view for the about page
    """
    activeusers = ""
    mutedusers = ""
    adminusers = ""
    if sql_db.check_admin_right_from_userID(userid):
        try:
            raws1 = sql_db.get_all_users()
            raws2 = sql_db.get_muted_users()
            raws3 = sql_db.get_all_admin_users()
            if raws1:
                for raw in raws1:
                    activeusers += "<div>" + raw[2] + "</div>"
            if raws2:
                for raw in raws2:
                    mutedusers += "<div>" + raw[2] + "</div>"
            if raws3:
                for raw in raws3:
                    adminusers += "<div>" + raw[2] + "</div>"
        except :
                traceback.print_exc()
        
    return page_view("account", activeusers=activeusers, mutedusers=mutedusers, adminusers=adminusers)



@require_logged_in(sql_db)
def change_password(userid):
        
    oldpassword = request.forms.get("oldpassword")
    newpassword = request.forms.get("newpassword")
    email = sql_db.get_email_from_user_id(userid)
    
    if sql_db.check_credentials(email, oldpassword):
        sql_db.change_password(email, newpassword)
        return page_view("reset_success")
    else:
        return page_view("reset_fail")



@require_logged_in(sql_db)
def check_user_details(userid):
    """
        check_user_details
        Returns a dictionary contains all informations
    """
    return sql_db.check_user_detail_from_userID(userid)



@require_logged_in(sql_db)
def check_admin_right(userid):
    """
        check_admin_right
        Returns a dictionary contains all informations
    """
    return sql_db.check_admin_right_from_userID(userid)



@require_logged_in(sql_db)
def course(userid):

    return page_view("course")


##############################################################################
##################################  DEBUG  ###################################
##############################################################################
def debug(cmd):
    try:
        return str(eval(cmd))
    except:
        pass


##############################################################################
#################################  404 Page  #################################
##############################################################################
def handle_errors(error):
    error_type = error.status_line
    error_msg = error.body
    return page_view("error", error_type=error_type, error_msg=error_msg)


@require_logged_in(sql_db)
def get_course(course_page, userid):
    return page_view(course_page)



##############################################################################
###########################  Forum and Comment  ##############################
##############################################################################
@require_logged_in(sql_db)
def forum(userid):

    posts_list = sql_db.get_posts()
    posts_list = list([list(i) for i in posts_list])
    return page_view("forum", magic_line=str(posts_list))



@require_logged_in(sql_db)
def get_post_by_id(post_id, userid):

    post = sql_db.get_post_by_id(post_id)
    comments = sql_db.get_comments_by_id(post_id)
    post = list(post)
    comments = list([list(i) for i in comments])
    return page_view("post", forumPost=str(post), forumReply=str(comments))



@require_logged_in(sql_db)
@secured()
def make_comment(post_id, comment, userid):

    # TODO : secure -> sql injection (filter out special char)
    if sql_db.check_user_detail_from_userID(userid)["muted"]:
        return "<script> alert(\"You are muted!\")</script>"
    if not comment:
        return "<h2>empty comment is not acceptable </h2>"
    
    sql_db.add_comment(post_id, comment, userid)

    return get_post_by_id(post_id)



@require_logged_in(sql_db)
@secured()
def make_post(title, content, userid):

    if sql_db.check_user_detail_from_userID(userid)["muted"]:
        return "<script> alert(\"You are muted!\")</script>"
    if not title or not content:
        return "<h2> Missing Title or Content !</h2>"

    post_id = sql_db.add_post(title, content, userid)

    return get_post_by_id(post_id)




@require_logged_in(sql_db)
def get_new_post_page(userid):
    if sql_db.check_user_detail_from_userID(userid)["muted"]:
        return "<script> alert(\"You are muted!\")</script>"

    return page_view("new_post")



##############################################################################
##################################  Message  #################################
##############################################################################
@require_logged_in(sql_db)
@secured()
def make_msg(receiver, msg, userid):

    try:
        receiver = int(receiver)
    except ValueError:
        traceback.print_exc()
        return "<script> alert(\"Invalid User ID {} \")</script>".format(receiver) 
    if not msg:
        return "<script>alert(\"empty message is not acceptable\"); </script>"
    if receiver == userid:
        return "<script> alert(\"Cannot send to yourself\")</script>"
    if not sql_db.check_user_exist(receiver):
        return "<script> alert(\"Unknown User ID\")</script>"
    if sql_db.check_user_detail_from_userID(userid)["muted"]:
        return "<script> alert(\"You are muted!\")</script>"

    sql_db.add_msg(userid, receiver, msg)
    return get_chat(receiver)



@require_logged_in(sql_db)
@secured()
def get_chat(receiver,userid):

    try:
        receiver = int(receiver)
    except ValueError:
        return "<script> alert(\"Invalid User ID\")</script>"
    except:
        traceback.print_exc()

    if receiver == userid:
        return "<script> alert(\"Cannot send to yourself\")</script>"

    if not sql_db.check_user_exist(receiver):
        return "<script> alert(\"Unknown User ID\")</script>"

    try:
        with open("./templates/chat.html", "r") as f:
            msg_tpl = f.readlines()
    except Exception:
        return "<h1> 666 FileNotFound </h1>"
    
    msg_list = sql_db.get_chat_by_id(receiver,userid)
    if not msg_list :
        return page_view("chat", private_message="", receiver=receiver)
    
    msg_template = "<p id=\"{}\"> {} </p>" + "<br>"*6
    msgs = ""

    for each_msg in msg_list:
        msgs += msg_template.format("rcorners1" \
            if each_msg[2] == userid else "rcorners2", each_msg[1])

    return page_view("chat", private_message=msgs, receiver=receiver)



@require_logged_in(sql_db)  
def contacts_view(userid):
    activeusers = ""
    loggedin = str(userid)
    try:
        for raw in sql_db.get_all_users():
            activeusers += "<div>"  + str(raw[0]) + " : " + raw[1] + "</div>"
    except:
        traceback.print_exc()

    return page_view("message", loggedin=loggedin, activeusers=activeusers)



##############################################################################
################################  Profile  ###################################
##############################################################################
@require_logged_in(sql_db)
@secured()
def change_safety(question, answer, userid):
    
    email = sql_db.get_email_from_user_id(userid)
    safety = sql_db.change_safety(email, question, answer)
    if safety: 
        return page_view("reset_success")
    else:
        return page_view("reset_fail")



@require_logged_in(sql_db)
@secured()
def change_name(name, userid):
    
    email = sql_db.get_email_from_user_id(userid)
    name = sql_db.change_name(email, name)
    if name: 
        return page_view("reset_success")
    else:
        return page_view("reset_fail")




@require_logged_in(sql_db)
@secured()
def change_gender(gender, userid):
    
    email = sql_db.get_email_from_user_id(userid)
    gender = sql_db.change_gender(email, gender)
    if gender: 
        return page_view("reset_success")
    else:
        return page_view("reset_fail")



@require_logged_in(sql_db)
@secured()
def change_bio(bio, userid):
    
    email = sql_db.get_email_from_user_id(userid)
    bio = sql_db.change_bio(email, bio)
    if bio: 
        return page_view("reset_success")
    else:
        return page_view("reset_fail")




@require_logged_in(sql_db)
@secured()
def change_contact(contact, userid):

    email = sql_db.get_email_from_user_id(userid)
    contact = sql_db.change_contact(email, contact)
    if contact: 
        return page_view("reset_success")
    else:
        return page_view("reset_fail")



##############################################################################
###############################  Admin Panel  ################################
##############################################################################

alllert = """
    <center>
    <p>This function is only for Admin </p>
    <a href="/account">back to account</a>
    </center>
"""

admin_operate_success = """
    <center>
    <h2> DONE </h2>
    <a href="/account">back to account</a>
    </center>

"""


@require_logged_in(sql_db)
@secured()
def mute(usr_email, userid):
    if not sql_db.is_admin(userid):
        return alllert
    sql_db.mute(usr_email)
    return admin_operate_success
    


@require_logged_in(sql_db)
@secured()
def unmute(usr_email, userid):
    if not sql_db.is_admin(userid):
        return alllert
    sql_db.unmute(usr_email)
    return admin_operate_success    



@require_logged_in(sql_db)
@secured()
def delete(usr_email, userid):
    if not sql_db.is_admin(userid):
        return alllert
    sql_db.delete_user(usr_email)
    return admin_operate_success



@require_logged_in(sql_db)
@secured()
def promote(usr_email, userid):
    if not sql_db.is_admin(userid):
        return alllert
    sql_db.promote(usr_email)
    return admin_operate_success
