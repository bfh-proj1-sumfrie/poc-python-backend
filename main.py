#!/usr/bin/python
import pymysql.cursors
import cherrypy
import json

@cherrypy.expose
class StringGeneratorWebService(object):

    @cherrypy.tools.accept(media='text/plain')
    def GET(self):
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='',
                                     db='sqlquery-poc',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)
        result = dict()
        try:
            with connection.cursor() as cursor:
                # Read a single record
                sql = "SELECT * FROM user_details"
                cursor.execute(sql)
                result = [dict(r) for r in cursor.fetchall()]
        finally:
            connection.close()
            return json.dumps(result, ensure_ascii=False)


if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],
        }
    }
    cherrypy.quickstart(StringGeneratorWebService(), '/', conf)
