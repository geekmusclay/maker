import datetime 

class Logger(object):
	HEADER    ='\033[95m'
	OKBLUE    = '\033[94m'
	OKGREEN   = '\033[92m'
	WARNING   = '\033[93m'
	FAIL      = '\033[91m'
	ENDC      = '\033[0m'
	BOLD      = '\033[1m'
	UNDERLINE = '\033[4m'

	def log_success(self, message):
		current_time = datetime.datetime.now() 
		print('[' + self.OKBLUE + str(current_time) + self.ENDC + '] : ' + self.OKGREEN + message + self.ENDC)
	
	def log_warning(self, message):
		current_time = datetime.datetime.now() 
		print('[' + self.OKBLUE + str(current_time) + self.ENDC + '] : ' + self.WARNING + message + self.ENDC)

	def log_fail(self, message):
		current_time = datetime.datetime.now() 
		print('[' + self.OKBLUE + str(current_time) + self.ENDC + '] : ' + self.FAIL + message + self.ENDC)
