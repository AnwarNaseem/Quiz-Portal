from marshmallow import Schema, fields, base

class APIResponse(Schema):
    message = fields.Str(default="Success")

class SignUpRequest(Schema):
    username = fields.Str(default = "username")
    password = fields.Str(default = "password")
    name = fields.Str(default = "name")
    is_admin = fields.Int(default = 0)

class LoginRequest(Schema):
    username = fields.Str(default="username")
    password = fields.Str(default="password")

class LogoutRequest(Schema):
    session_id = fields.Str(default="session_id")

class QuestionsRequest(Schema):
    session_id = fields.Str(default="session_id")

class ListQuestionsResponse(Schema):
    questions = fields.List(fields.Dict())

class ListQuestionsResquest(Schema):
    question = fields.Str(default="question")

class AddQuestionRequest(Schema):
    session_id = fields.Str(default="session_id")
    question = fields.Str(default="question")
    choice1 = fields.Str(default="choice1")
    choice2 = fields.Str(default="choice2")
    choice3 = fields.Str(default="choice3")
    choice4 = fields.Str(default="choice4")
    marks = fields.Int(default=0)
    remarks = fields.Str(default="remarks")

class CreateQuizRequest(Schema):
    user_id = fields.Int(default="user_id")
    session_id = fields.Str(default="session_id")
    quiz = fields.Str(default="quiz_id")

class ListQuizRequest(Schema):
    questions = fields.List(fields.Dict())

class ViewQuizResponse(Schema):
    quiz_id = fields.List(fields.Dict())

class ViewQuizRequest(Schema):
    quiz_id = fields.Str(default="quiz_id")
     
class AssignedQuizRequest(Schema):
    user_id = fields.Str(default="user_id")
    session_id = fields.Str(default="session_id")
    quiz_id = fields.Str(default="quiz_id")
  
class AssignedQuizResponse(Schema):
    user_id = fields.List(fields.Dict())
    quiz_id = fields.List(fields.Dict())

class ViewAllQuizResponse(Schema):
     quiz_id = fields.List(fields.Dict())

class ViewAllQuizRequest(Schema):
    quiz_id = fields.Str(default="quiz_id")

class AttemptQuizResponse(Schema):
    response = fields.List(fields.Dict())

class AttemptQuizRequest(Schema):
    user_id = fields.Str(default="user_id")
    quiz_id = fields.Str(default="quiz_id")
    response = fields.Str(default="response")

class QuizResultResponse(Schema):
    score_achieved = fields.List(fields.Dict())

class QuizResultRequest(Schema):
    user_id = fields.Str(default="user_id")
    quiz_id = fields.Str(default="quiz_id")
    score_achieved = fields.Str(default="score_achieved")

"""
This module aims at providing the request and response format for the various api calls.
This also helpful for creating swagger docs for apis testing.
"""
