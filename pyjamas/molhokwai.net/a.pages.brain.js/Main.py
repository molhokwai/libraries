import pyjd # this is dummy in pyjs.
import pygwt

from Index import Index

if __name__ == '__main__':
	pyjd.setup("public/Main.html")
	app = Index()
	app.onModuleLoad()
	pyjd.run()


