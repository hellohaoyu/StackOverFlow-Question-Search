import logging
import webapp2
import jinja2


class SearchHandler(webapp2.RequestHandler):
	def post(self):
		self.response.write('This is title from search')
		# logging.info("Get MainPage")
  #       template_value = {}
  #       template_value['data'] = [{'Title': "This is question title"}]
  #       template = jinja_environment.get_template('index.html')
        # self.response.write(template.render(template_value))
	# 	logging.info("Post MainPage" )
	# 	global template_value
	# 	template_value['is_Login'] = True
	# 	template_value['name'] = self.request.get("Name")
	# 	template_value['ID'] = self.request.get("ID")
	# 	self.redirect('/')
	# 	qry = Player.query(Player.userid == self.request.get("ID"))
	# 	# logging.info(Player.get_by_id(self.request.get("ID")))
	# 	playerid = (self.request.get("ID"))
	# 	# logging.info(qry.get())
	# 	# logging.info("AddExperiment")
	# 	if (qry.get() == None) and (self.request.get("Type") == "AddUser") :
	# 		logging.info("AddUser")
	# 		self.player = Player(parent=ndb.Key("Players", "PlayersKeys"), name = self.request.get("Name"), userid = playerid)
	# 		self.player.put()

	# 	if (self.request.get("Type") == "AddExperiment"):
	# 		logging.info("AddExperiment")
	# 		self.experiment = Experiment(parent=ndb.Key("Experiments", self.request.get("ID")), userid = playerid, time = self.request.get("TimeCost"))
	# 		myplayer = qry.get()
	# 		myplayer.experiments.append(self.experiment)
	# 		myplayer.put()

	# 	template_value['is_Play_CoinGame'] = False
	# 	template_value['is_Play_DiskGame'] = False
	# 	logging.info("*****************************************")
	# 	logging.info((str)(self.request.get("GameId")) == '1')
	# 	logging.info(self.request.get("GameId") == 1)
	# 	# if self.request.get("GameId") ==  1:
	# 	if (str)(self.request.get("GameId")) == '1':
	# 		template_value['is_Play_CoinGame'] = True
	# 	else:
	# 		template_value['is_Play_DiskGame'] = True