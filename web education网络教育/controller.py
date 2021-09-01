from bottle import route, get, post, error, request, static_file

import model



##############################################################################
##############################  Static Files  ################################
##############################################################################


@route("/img/<picture:path>")
def serve_pictures(picture):

    return static_file(picture, root="static/img/")



@route("/css/<css:path>")
def serve_css(css):

    return static_file(css, root="static/css/")



@route("/js/<js:path>")
def serve_js(js):
    return static_file(js, root="static/js/")



@route("/fonts/<fonts:path>")
def serve_js(fonts):
    return static_file(fonts, root="static/fonts/")




@get("/check_user_details")
def check_user_details():
    return model.check_user_details()



@get("/check_admin_right")
def check_admin_right():
    return model.check_admin_right()



##############################################################################
############################  Login and Sign up   ############################
##############################################################################


@get("/login")
def get_login_controller():

    return model.login_form()



@post("/login")
def post_login():

    email = request.forms.get("email")
    password = request.forms.get("password")
    
    return model.login_check(email, password)



@get("/signup")
def get_signup_controller():

    return model.sign_up_form()



@post("/signup")
def post_signup():

    email = request.forms.get("email")
    password = request.forms.get("password")
    confirmpassword = request.forms.get("confirmpassword")

    if password != confirmpassword:
        return "<script>alert(\"Password does not match!\")</script>"

    displayname = request.forms.get("displayname")
    question = request.forms.get("question")
    answer =  request.forms.get("answer")
    
    return model.sign_up(email, password, displayname, question, answer)


##############################################################################
##################################  Pages  ###################################
##############################################################################

@get("/")
@get("/home")
def get_index():
    return model.login_form()



@get("/course")
def get_course():

    return model.course()



@get("/course/<course_page>")
def get_course_page(course_page):

    return model.get_course(course_page)



@get("/feed")
def feed():

    return model.feed()



@get("/forum")
def get_forum_page():

    return model.forum()



@get("/forum/<post_id>")
def get_forum_page_id(post_id):

    print("getting post_id{}".format(post_id))
    return model.get_post_by_id(post_id)



@post("/forum/<post_id>")
def make_comment(post_id):

    comment = request.forms.get("cmt")
    return model.make_comment(post_id, comment)



@get("/new_post")
def get_new_post_page():
    return model.get_new_post_page()



@post("/new_post")
def make_post():

    post_title = request.forms.get("title")
    post_content = request.forms.get("new_post")

    return model.make_post(post_title, post_content)



@get("/message")
def get_message_page():
    return model.contacts_view()



@post("/message")
def view_chat():
    receiver = request.forms.get("receiver")

    return model.get_chat(receiver)



@post("/chat")
def send_message():
    msg = request.forms.get("msg")
    receiver = request.forms.get("receiver")

    return model.make_msg(receiver, msg)



@get("/account")
def get_account():
    return model.account()



@post("/debug/<cmd:path>")
def post_debug(cmd):
    return "Interesting\n"
    # return model.debug(cmd)



##############################################################################
###########################  Profile Settings  ###############################
##############################################################################


@post("/changebio")
def post_change_bio():

    bio = request.forms.get("newbio")

    return model.change_bio(bio)



@post("/changepassword")
def change_password():

    return model.change_password()



@post("/changesafety")
def post_change_safety():

    question = request.forms.get("question")
    answer =  request.forms.get("answer")

    return model.change_safety(question, answer)



@post("/changename")
def post_change_name():

    name = request.forms.get("newname")
    return model.change_name(name)



@post("/changegender")
def post_change_gender():

    gender = request.forms.get("newgender")
    return model.change_gender(gender)



@post("/changecontact")
def post_change_contact():

    contact = request.forms.get("newcontact")
    return model.change_contact(contact)



@get("/logout")
def get_logout_page():
    return model.log_out()



##############################################################################
#############################  Only For admins  ##############################
##############################################################################


@post("/promote")
def promote():
    # TODO : find element
    usr_email = request.forms.get("email")
    return model.promote(usr_email)



@post("/mute")
def mute():
    # TODO : find element
    usr_email = request.forms.get("email")
    return model.mute(usr_email)



@post("/unmute")
def unmute():
    # TODO : find element
    usr_email = request.forms.get("email")
    return model.unmute(usr_email)



@post("/delete")
def delete():
    # TODO : find element
    usr_email = request.forms.get("email")
    return model.delete(usr_email)



##############################################################################
###################################  404  ####################################
##############################################################################


@error(404)
def error(error): 
    return model.handle_errors(error)
