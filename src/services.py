from sqlalchemy.orm.session import sessionmaker
from models import QuestionMaster, QuizInstance, QuizMaster, QuizQuestions, UserMaster, UserResponses, UserSession
from app import db
import uuid
from flask import session
import datetime
from typing import List

"""
[Services Module] Implement various helper functions here as a part of api
                    implementation using MVC Template
"""
def create_user(**kwargs):
    try:
        user= UserMaster(
                    uuid.uuid4(),
                    kwargs['name'],
                    kwargs['username'],
                    kwargs['password'],
                    kwargs['is_admin'],
                    )
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        raise e

def login_user(**kwargs):
    try:
        user = UserMaster.query.filter_by(username=kwargs['username'],password=kwargs['password']).first()
        if user:
            print("Logged in successfully")
            is_active, session_id = check_user_session_is_active(user.id)
            if not is_active:
                session_id = uuid.uuid4()
                user_session = UserSession(uuid.uuid4(), user.id,session_id)
                db.session.add(user_session)
                db.session.commit()
            else:
                session['session_id'] = session_id
            session['session_id'] = session_id
            return True, session_id
        else:
            return False, None
    except Exception as e:
        raise e

def check_user_session_is_active(user_id):
    try:
        user_session=UserSession.query.filter_by(user_id=user_id,is_active=1).first()
        if user_session:
            return True,user_session.session_id
        else:
            print("User not found")
            return False, None
    except Exception as e:
        raise e

def check_if_admin(is_admin):
    try:
        user_session=UserMaster.query.filter_by(is_admin=is_admin,is_active=1).first()
        if is_admin:
            return True,user_session.session_id
        else:
            print("User is not admin")
            return False, None
    except Exception as e:
        raise e

def add_question(**kwargs):
    try:
        question=QuestionMaster(
            uuid.uuid4(),
            kwargs['question'],
            kwargs['choice1'],
            kwargs['choice2'],
            kwargs['choice3'],
            kwargs['choice4'],
            kwargs['answer'],
            kwargs['marks'],
            kwargs['remarks']
        )
        db.session.add(question)
        db.session.commit()
    except Exception as e:
        raise e

def create_quiz(**kwargs):
    try:
        quiz=QuestionMaster(
            uuid.uuid4(),
            kwargs['id'],
            kwargs['quiz_name'],
            kwargs['created_ts']      
        )
        db.session.add(quiz)
        db.session.commit()
    except Exception as e:
        raise e

def list_questions(**kwargs):
    try:
        list_questions=QuizQuestions.query.filter_by(question_id=kwargs['question_id']).first()
        if list_questions:
            for question in list_questions:
                print("Questions in the quiz,")
                print(question)
            return True, list_questions
        else:
            print("Error in listing questions")
    except Exception as e:
        raise e

def assign_quiz(**kwargs):
    try:
        assign_quiz=QuizInstance.query.filter_by(user_id=kwargs['user_id'],quiz_id=kwargs['quiz_id']).first()
        user_id=kwargs['user_id']
        if assign_quiz(user_id):
            user_id=kwargs['user_id']
            quiz_id=kwargs['quiz_id']
            assign_quiz=QuizInstance(user_id,quiz_id)
            print("Quiz assigned to the user")
            return True, assign_quiz
        else:
            print("Cannot assign quiz")
    except Exception as e:
        raise e

def check_quiz_access(quiz_id):
    try:
        quiz_access=QuizInstance.query.filter_by(user_id=['user_id'],quiz_id=['quiz_id']).first()
        if quiz_access:
            quiz_id['quiz_id'] = quiz_id
            return True, quiz_access
        else:
            print("User does not have access")
    except Exception as e:
        raise e
    
def view_quiz(user_id):
    try:
        view_quiz=QuizMaster.query.filter_by(quiz_name=['quiz_name'],created_ts=['created_ts']).first()
        if view_quiz:
            view_quiz = check_quiz_access(user_id)
            return True, view_quiz
        else:
            print("user does not have access")
    except Exception as e:
        raise e

def view_assigned_quiz(**kwargs):
    try:
        view_assigned_quiz=QuizInstance.query.filter_by(unique_quiz_user=kwargs['unique_quiz_user']).first()
        if view_assigned_quiz(user_id):
            user_id=kwargs['user_id']
            quiz_id=kwargs['quiz_id']
            view_assigned_quiz=QuizInstance(quiz_id,user_id)
            return True, view_assigned_quiz
        else:
            print("cannot view assigned quiz")
    except Exception as e:
        raise e

def attempt_quiz():
    try:
        attempt_quiz=QuizMaster.query.filter_by(question=['question'],answer=['answer'],marks=['marks']).first()
        if attempt_quiz:
            question=['question']
            answer=['answer']
            marks=['marks']
            attempt_quiz=QuizMaster(question,answer,marks)
            return True, attempt_quiz
        else:
            print("Cannot view quiz")
    except Exception as e:
        raise e

def quiz_results(**kwargs):
    try:
        results=QuizInstance.query.filter_by(unique_quiz_user=kwargs['unique_quiz_user'],score=kwargs['score_achieved']).first()
        if results:
            user_id=kwargs['user_id']
            quiz_id=kwargs['quiz_id']
            score_achieved=kwargs['score_achieved']
            results=QuizInstance(user_id,quiz_id,score_achieved)
            print("score achieved:")
            return True, results
        else:
            print("Error in fetching the quiz results")
    except Exception as e:
        raise e

def get_all_quiz_info(**kwargs):
    try:
        get_all_quiz_info=UserResponses.query.filter_by(unique_quiz_user_question=kwargs['unique_quiz_user_question'],response=kwargs['response']).first()
        if get_all_quiz_info:
            quiz_id=kwargs['quiz_id']
            user_id=kwargs['user_id']
            question_id=kwargs['question_id']
            response=kwargs['response']
            get_all_quiz_info=UserResponses(quiz_id,user_id,question_id,response,)
            print("Quiz Details")
            return True, get_all_quiz_info
        else:
            print("Unable to fetch data")
    except Exception as e:
        raise e

def logout_user(session_id):
    try:
        user_session=UserSession.query.filter_by(session_id=['session_id'],is_active=1).first()
        if user_session:
            is_active, session_id = check_user_session_is_active(session_id)
            if is_active:
                session_id = uuid.uuid4()
                user_session = UserSession(uuid.uuid4(),session_id)
                print("Logged out successfully")
            else:
                session['session_id'] = session_id
            session['session_id'] = session_id
        return True, session_id
    except Exception as e:
        raise e