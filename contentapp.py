#!/usr/bin/python
import webapp


class contentApp (webapp.webApp):

    # Variable de clase
    content = {'/': 'Root page',
               '/page': 'A page',
               '/pepe': 'Hola',
               '/nueva':'Otra mas'
               }

    def parse(self, request):
        
        herader = request.split(' ', 1)[0]  # metodo
        request = request.split(' ', 2)[1]  # recurso
        try
            body = request.split()[-1]  # body = request.split('\r\n\r\n')[1]
        except IndexError:
            body = ""
        return [header, request, body]

    def process(self, resourceName):

        metodo, recurso, cuerpo = peticion
        if metodo == "GET":
            if recurso in self.content: # self.content.keys()
                httpCode = "200 OK"
                htmlBody = "<html><body>" + self.content[resourceName] \
                    + "</body></html>"
            else:
                httpCode = "404 Not Found"
                htmlBody = "Not Found"
        elif metodo == "PUT" or metodo == "POST"
            self.content[recurso] = cuerpo
            httpCode = "200 OK"
            htmlBody = "Todo ha ido bien"
        else
            httpCode = "450 Method Not Allowed"
            htmlBody = "Go away!"
        return (httpCode, htmlBody)

if __name__ == "__main__":
    testWebApp = contentApp("localhost", 1235)
