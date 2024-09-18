from framework.services.service_factory import BaseServiceFactory
import app.resources.course_resource as course_resource
from framework.services.data_access.MySQLRDBDataService import MySQLRDBDataService
import yaml


# TODO -- Implement this class
class ServiceFactory(BaseServiceFactory):

    def __init__(self):
        super().__init__()

    @classmethod
    def get_service(cls, service_name):
        #
        # TODO -- The terrible, hardcoding and hacking continues.
        #
        if service_name == 'CourseResource':
            result = course_resource.CourseResource(config=None)
        elif service_name == 'CourseResourceDataService':
            with open("app/config/database.yaml", "r") as file:
                db_config = yaml.load(file, Loader=yaml.FullLoader)
            user  = db_config["user"] if "user" in db_config else "root"
            password = db_config["password"] if "password" in db_config else "dbuserdbuser"
            context = dict(user=user, password=password,
                           host="localhost", port=3306)
            data_service = MySQLRDBDataService(context=context)
            result = data_service
        else:
            result = None

        return result




