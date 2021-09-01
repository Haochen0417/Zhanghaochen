import sqlite3
from datetime import datetime
from datetime import timedelta
import uuid 



class SQLDatabase():
    '''
        Our SQL Database

    '''

    # Get the database running
    def __init__(self, database_arg=":memory:"):
        self.conn = sqlite3.connect(database_arg)
        self.cur = self.conn.cursor()

    # SQLite 3 does not natively support multiple commands in a single statement
    # Using this handler restores this functionality
    # This only returns the output of the last command
    def execute(self, sql_string):
        out = None
        for string in sql_string.split(";"):
            # out = self.cur.execute(string)
            try:
                out = self.cur.execute(string)
            except:
                print("error on",)
        return out

    # Commit changes to the database
    def commit(self):
        self.conn.commit()

    #-----------------------------------------------------------------------------
    
    # Sets up the database
    # Default admin password
    def database_setup(self, admin_password='admin'):

        # Clear the database if needed
        self.execute("DROP TABLE IF EXISTS Users_caonidezui")
        self.execute("DROP TABLE IF EXISTS Forum_caonidezui")
        self.execute("DROP TABLE IF EXISTS PrivateMessage_caonidezui")
        self.execute("DROP TABLE IF EXISTS Sessions_caonidezui")
        self.execute("DROP TABLE IF EXISTS Message_caonidezui")
        self.execute("DROP TABLE IF EXISTS ForumPost_caonidezui")
        self.execute("DROP TABLE IF EXISTS ForumReply_caonidezui")
        self.execute("DROP TABLE IF EXISTS Safety_caonidezui")
        self.commit()

        # Create the users table
        self.execute(
            """
            CREATE TABLE Users_caonidezui(
                Id INTEGER PRIMARY KEY AUTOINCREMENT,
                DisplayName TEXT,
                Email TEXT UNIQUE,
                Password TEXT,
                Gender TEXT Default "Unknown",
                Bio TEXT Default "Without Setting",
                Contact TEXT Default "Unknow",
                Muted INTEGER DEFAULT 0,
                Admin INTEGER DEFAULT 0
            );
            """
        )

        # Create the users' safety table
        self.execute(
            """
            CREATE TABLE Safety_caonidezui(
                UserId TEXT PRIMAR KEY,
                Question TEXT,
                Answer TEXT,
                FOREIGN KEY(UserId) REFERENCES Users_caonidezui(Id)
            );
            """
        )

        #Create Private Messages table
        self.execute(
            """
            CREATE TABLE PrivateMessage_caonidezui(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                message VARCHAR(255) NOT NULL,
                sender INTEGER REFERENCES Users_caonidezui(Id) NOT NULL,
                receiver INTEGER REFERENCES Users_caonidezui(Id) NOT NULL,
                time TimeStamp NOT NULL DEFAULT (datetime('now','localtime'))
            );
            """
        )
        
        # Create sessions table
        self.execute(
            """
            CREATE TABLE Sessions_caonidezui(
                ID TEXT PRIMAR KEY,
                UserId INTEGER,
                CreatedTime TEXT,
                ExpireTime TEXT,
                LastModified TEXT,
                IP TEXT,
                FOREIGN KEY(UserId) REFERENCES Users_caonidezui(Id)
            );
            """
        )
        # # Create the forum table
        self.execute("""
            CREATE TABLE ForumPost_caonidezui(
                postID INTEGER PRIMARY KEY AUTOINCREMENT,
                UID INTEGER NOT NULL REFERENCES Users_caonidezui(Id),
                title TEXT Not NULL,
                content TEXT NOT NULL,
                time TimeStamp NOT NULL DEFAULT (datetime('now','localtime'))
            );
        """)

        self.execute("""
            CREATE TABLE ForumReply_caonidezui(
                replyID INTEGER PRIMARY KEY AUTOINCREMENT,
                postID INTEGER NOT NULL REFERENCES ForumPost_caonidezui(postID),
                UID INTEGER NOT NULL REFERENCES Users_caonidezui(Id),
                content TEXT NOT NULL,
                time TimeStamp NOT NULL DEFAULT (datetime('now','localtime'))
            );
        
        """)

        self.commit()

        # Add our admin user
        self.add_user("admin@sydney.edu.au", admin_password, 'admin', admin=1)
        self.execute("""
        INSERT INTO ForumPost_caonidezui(UID, title, content)
        VALUES (1, 'Thread1', 'Content1')
        """)
        self.execute("""
        INSERT INTO ForumPost_caonidezui(UID, title, content)
        VALUES (1, 'hhhhhhh', 'Content of hhhhhhhhhhh')
        """)
        self.execute("""
        INSERT INTO ForumReply_caonidezui(postID, UID, content)
        VALUES (1, 1, 'Reply1_1')
        """)
        self.commit()
    #-----------------------------------------------------------------------------
    # User handling
    #-----------------------------------------------------------------------------

    # Add a user to the database
    def add_user(self, email, password, displayName, admin=0):

        sql_cmd ="""
                INSERT INTO Users_caonidezui('DisplayName', 'Email', 'Password', 'Muted', 'Admin')
                VALUES('{displayName}', '{email}', '{password}', {Muted}, {admin})
            """

        sql_cmd = sql_cmd.format(displayName=displayName, email=email, password=password, Muted=0, admin=admin)

        self.execute(sql_cmd)
        self.commit()
        return True


    #-----------------------------------------------------------------------------

    # Add a safety question to the database
    def set_safety(self, email, question, answer):


        uid = self.get_user_id_from_email(email)

        sql_cmd ="""
                INSERT INTO Safety_caonidezui('UserId', 'Question', 'Answer')
                VALUES('{uid}', '{question}', '{answer}')
            """

        sql_cmd = sql_cmd.format(uid=uid, question=question, answer=answer)

        self.execute(sql_cmd)
        self.commit()
        return True

    #-----------------------------------------------------------------------------

    #-----------------------------------------------------------------------------

    # change a safety question for the database
    def change_safety(self, email, question, answer):

        uid = self.get_user_id_from_email(email)

        sql_cmd ="""
            UPDATE Safety_caonidezui SET Question = '{question}' WHERE UserId = '{uid}'; 
            UPDATE Safety_caonidezui SET Answer = '{answer}' WHERE UserId = '{uid}' 
            """

        sql_cmd = sql_cmd.format(uid=uid, question=question, answer=answer)

        self.execute(sql_cmd)
        self.commit()
        return True

    #-----------------------------------------------------------------------------

    #-----------------------------------------------------------------------------

    # change a safety question for the database
    def change_name(self, email, name):

        uid = self.get_user_id_from_email(email)

        sql_cmd ="""
            UPDATE Users_caonidezui SET DisplayName = '{name}' WHERE Id = '{uid}'; 
            """

        sql_cmd = sql_cmd.format(uid=uid, name=name)

        self.execute(sql_cmd)
        self.commit()
        return True

    #-----------------------------------------------------------------------------

    #-----------------------------------------------------------------------------

    # change a gender for the database
    def change_gender(self, email, gender):

        uid = self.get_user_id_from_email(email)

        sql_cmd ="""
            UPDATE Users_caonidezui SET Gender = '{gender}' WHERE Id = '{uid}'; 
            """

        sql_cmd = sql_cmd.format(uid=uid, gender=gender)

        self.execute(sql_cmd)
        self.commit()
        return True

    #-----------------------------------------------------------------------------

    #-----------------------------------------------------------------------------

    # change a gender for the database
    def change_bio(self, email, bio):

        uid = self.get_user_id_from_email(email)

        sql_cmd ="""
            UPDATE Users_caonidezui SET Bio = '{bio}' WHERE Id = '{uid}'; 
            """

        sql_cmd = sql_cmd.format(uid=uid, bio=bio)

        self.execute(sql_cmd)
        self.commit()
        return True

    #-----------------------------------------------------------------------------

    #-----------------------------------------------------------------------------

    # change a gender for the database
    def change_contact(self, email, contact):

        uid = self.get_user_id_from_email(email)

        sql_cmd ="""
            UPDATE Users_caonidezui SET contact = '{contact}' WHERE Id = '{uid}'; 
            """

        sql_cmd = sql_cmd.format(uid=uid, contact=contact)

        self.execute(sql_cmd)
        self.commit()
        return True

    #-----------------------------------------------------------------------------

    #-----------------------------------------------------------------------------
    # Delete a user from the database
    def delete_user(self, email):
        sql_cmd ="""
                DELETE FROM Users_caonidezui
                WHERE Email = '{email}'
            """

        sql_cmd = sql_cmd.format(email=email)

        self.execute(sql_cmd)
        self.commit()
        if self.cur.fetchone():
            return True
        else:
            return False
    #-----------------------------------------------------------------------------
   
    def mute(self, email):
        sql_cmd ="""
            UPDATE Users_caonidezui
            SET Muted = 1 
            WHERE Email = '{email}'
            """

        sql_cmd = sql_cmd.format(email=email)
        self.execute(sql_cmd)
        self.commit()
        return True

    #-----------------------------------------------------------------------------
    
    def unmute(self, email):
        sql_cmd ="""
            UPDATE Users_caonidezui
            SET Muted = 0
            WHERE Email = '{email}'
            """

        sql_cmd = sql_cmd.format(email=email)
        self.execute(sql_cmd)
        self.commit()
        return True

    #-----------------------------------------------------------------------------
    
    def promote(self, email):
        sql_cmd ="""
            UPDATE Users_caonidezui
            SET Admin = 1
            WHERE Email = '{email}'
            """

        sql_cmd = sql_cmd.format(email=email)
        self.execute(sql_cmd)
        self.commit()
        return True

    #-----------------------------------------------------------------------------
    

    def demote(self, email):
        sql_cmd ="""
            UPDATE Users_caonidezui
            SET Admin = 0
            WHERE Email = '{email}'
            """

        sql_cmd = sql_cmd.format(email=email)
        self.execute(sql_cmd)
        self.commit()
        return True

    #-----------------------------------------------------------------------------

    def get_user_id_from_email(self, email):
        sql_query ="""
                SELECT Id
                FROM Users_caonidezui
                WHERE Email = '{email}'
            """

        sql_query = sql_query.format(email=email)
        self.execute(sql_query)
        res = self.cur.fetchone()

        if res:
            return res[0]
        else:
            return False

    def get_email_from_user_id(self, id):
        sql_query ="""
                SELECT Email
                FROM Users_caonidezui
                WHERE Id = '{id}'
            """

        sql_query = sql_query.format(id=id)
        self.execute(sql_query)
        res = self.cur.fetchone()

        if res:
            return res[0]
        else:
            return False

    # Check login credentials
    def check_credentials(self, email, password):
        sql_query ="""
                SELECT *
                FROM Users_caonidezui
                WHERE Email = '{email}' AND Password = '{password}'
            """

        sql_query = sql_query.format(email=email, password=password)
        self.execute(sql_query)

        res = self.cur.fetchone()

        # If our query returns
        if res:
            return res
        else:
            return False


    def create_session(self, email, remote_addr):
        '''
        :param email: the email of the user attempt to login
        return SESSIONID
        '''
        Userid = self.get_user_id_from_email(email)
        SESSIONID = uuid.uuid4().hex[:17].upper()
        sql_cmd ="""
                INSERT INTO Sessions_caonidezui('ID', 'UserId', 'CreatedTime', 'ExpireTime', 'LastModified', 'IP')
                VALUES('{ID}', '{Userid}', '{CreatedTime}', '{ExpireTime}', '{LastModified}', '{IP}')
            """

        CreatedTime = datetime.now()
        ExpireTime = datetime.now() + timedelta(minutes=15) 

        sql_cmd = sql_cmd.format(ID=SESSIONID, Userid=Userid, CreatedTime=CreatedTime, ExpireTime=ExpireTime, LastModified=CreatedTime, IP=remote_addr)

        self.execute(sql_cmd)
        self.commit()
        return SESSIONID, ExpireTime

        

    def get_user_id_from_session(self, SESSIONID):
        '''
        :param SESSIONID: Associated id of session returned from client

        RETURN the user id, 'Id' in 'Users' table
        '''
        sql_query ="""
                SELECT UserId
                FROM Sessions_caonidezui
                WHERE ID = '{SESSIONID}'
            """
        sql_query = sql_query.format(SESSIONID=SESSIONID)
        self.execute(sql_query)
        res = self.cur.fetchone()
        # If our query returns
        if res:
            return res[0]
        else:
            return False


    def get_posts(self, num=100):
        sql_query =  """
                SELECT postID, UID, title
                FROM ForumPost_caonidezui
        """
        self.execute(sql_query)
        res = self.cur.fetchall()
        if not res:
            return []
        if len(res) > num:
            res = res[0:num]
        return res


    def get_post_by_id(self, post_id):
        sql_query =  """
                SELECT postID, DisplayName, title, content, time
                FROM ForumPost_caonidezui natural join Users_caonidezui
                where ForumPost_caonidezui.postID = {id}
        """
        self.execute(sql_query.format(id=post_id))
        res = self.cur.fetchone()

        if not res:
            return []

        return res
   
    #message
    def get_chat_by_id(self, receiver,userid):
        sql_query =  """
                SELECT ID, message, sender, receiver
                FROM PrivateMessage_caonidezui 
                where 
                PrivateMessage_caonidezui.receiver = {name} and PrivateMessage_caonidezui.sender={uid}
                OR 
                PrivateMessage_caonidezui.receiver = {uid} and PrivateMessage_caonidezui.sender={name}
                ORDER BY time
        """

        self.execute(sql_query.format(name=receiver,uid=userid))
        res = self.cur.fetchall()
        print("get chat by id: ")
        print(res)
        if not res:
            return []
        return res




    def get_comments_by_id(self, post_id, num=100):
        sql_query =  """
                SELECT replyID, postID, DisplayName, content, time
                FROM ForumReply_caonidezui join Users_caonidezui ON Users_caonidezui.Id = ForumReply.UID
                where ForumReply_caonidezui.postID = {id}
        """
        self.execute(sql_query.format(id=post_id))
        res = self.cur.fetchall()
        for _ in res:
            print(_)
        print(res)
        if not res:
            return []
        if len(res) > num:
            res = res[0:num]
        return res



    def add_comment(self, post_id, comment, uid=1):
        sql_query = """
            INSERT INTO ForumReply_caonidezui(postID, UID, content)
            VALUES ({postID}, {UID}, '{content}')
        """
        self.execute(sql_query.format(postID=post_id, UID=uid, content=comment))
        self.commit()
    

    #message
    def add_msg(self, sender, receiver, msg, uid=1):
        sql_query = """
            INSERT INTO PrivateMessage_caonidezui(message, sender, receiver)
            VALUES ('{message}', {sender}, {receiver})
        """
        print(sender)
        print(receiver)
        print(msg)
        self.execute(sql_query.format(message=msg , sender=sender , receiver=receiver))
        self.commit()



    def add_post(self, post_title, post_content, uid=1):
        sql_query = """
            INSERT INTO ForumPost_caonidezui(UID, title, content)
            VALUES ({UID}, '{title}', '{content}')
        """

        self.execute(sql_query.format(UID=uid, title=post_title, content=post_content))
        self.commit()
        sql_query = """
            SELECT max(postID)
            from ForumPost_caonidezui
        """
        self.execute(sql_query)
        res = self.cur.fetchone()
        return res[0]



    def session_is_expire(self, SESSIONID):
        sql_query ="""
                SELECT ExpireTime
                FROM Sessions_caonidezui
                WHERE ID = '{SESSIONID}'
            """

        sql_query = sql_query.format(SESSIONID=SESSIONID)
        self.execute(sql_query)
        res = self.cur.fetchone()
        if res:
            expiretime = datetime.strptime(res[0].split('.')[0], '%Y-%m-%d %H:%M:%S')
            now = datetime.now()
            if now > expiretime:
                return True
            else:
                return False
        return True



    def update_expire_time(self, SESSIONID):
        sql_cmd = """
                UPDATE Sessions_caonidezui
                SET LastModified = '{new_LastModified}', ExpireTime = '{new_ExpireTime}'
                WHERE ID = '{SESSIONID}'
            """
        new_LastModified = datetime.now()
        new_ExpireTime = new_LastModified + timedelta(minutes=15) 
        sql_cmd = sql_cmd.format(new_LastModified=new_LastModified,\
             new_ExpireTime=new_ExpireTime, SESSIONID=SESSIONID)
        self.execute(sql_cmd)
        self.commit()
        return new_LastModified, new_ExpireTime



    def check_user_detail_from_userID(self, userID):
        '''
        :param userID: Associated id of user id returned from client

        RETURN all the information in 'Users' table
        '''

        sql_cmd = """
                select DisplayName, Email, Gender, Bio, Contact, Muted
                from Users_caonidezui
                where id = '{userID}'
            """
        sql_cmd = sql_cmd.format(userID=userID)
        self.execute(sql_cmd)
        res = self.cur.fetchone()
        # If our query returns
        if res:
            return {
                "name": res[0], "email"  : res[1], "gender": res[2],
                "bio" : res[3], "contact": res[4], "muted" : res[5]
                }
        else:
            return False
    


    def check_admin_right_from_userID(self, userID):
        '''
        :param userID: Associated id of user id returned from client

        RETURN adminToken in 'Users' table
        '''

        sql_cmd = """
                select Admin
                from Users_caonidezui
                where id = '{userID}'
            """
        sql_cmd = sql_cmd.format(userID=userID)
        self.execute(sql_cmd)
        res = self.cur.fetchone()

        if res:
            return str(res[0])
        else:
            return False
    


    def change_password(self, email, password):
        
        sql_cmd = """
                UPDATE Users_caonidezui
                SET Password = '{password}'
                WHERE Email = '{email}'
            """
        sql_cmd = sql_cmd.format(password=password, email=email)
        self.execute(sql_cmd)
        self.commit()
        return True
    


    def get_all_users(self):

        sql_query="""
            SELECT *
            FROM Users_caonidezui
        """
        self.execute(sql_query)
        res = self.cur.fetchall()

        if res:
            return res
        else:
            return False
    


    def get_muted_users(self):
        sql_query="""
            SELECT *
            FROM Users_caonidezui
            WHERE Muted = 1
        """
        self.execute(sql_query)
        res = self.cur.fetchall()

        if res:
            return res
        else:
            return False

    

    def get_all_admin_users(self):
        sql_query="""
            SELECT *
            FROM Users_caonidezui
            WHERE Admin = 1
        """
        self.execute(sql_query)
        res = self.cur.fetchall()

        return res if res else False



    def is_admin(self, userid):

        sql_cmd = """
            SELECT Users_caonidezui.Admin
            FROM Users_caonidezui
            WHERE Id = {userid} and Users_caonidezui.Admin = 1
        """
        self.execute(sql_cmd.format(userid=userid))
        res = self.cur.fetchone()

        return res != None

    def check_user_exist(self, userid):
        return self.check_user_detail_from_userID(userid)
    
    def check_db(self):
        sql_query = """
            SELECT name 
            FROM sqlite_master 
            WHERE type= "table"
        """

        self.execute(sql_query)
        res = self.cur.fetchall()
        print("Available Tables:")
        for r in res[1:]:
            print(r[0], end=', ')
        table=input("\nType table name to query:\n")
        
        sql_query = """
            SELECT *
            FROM {table}
        """
        self.execute(sql_query.format(table=table.strip()))

        res = self.cur.fetchall()
        for entry in res:
            print(entry)
        