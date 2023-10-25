from flask import Flask

app = Flask(__name__)

import routes.frontpage
import routes.login
import routes.signup
