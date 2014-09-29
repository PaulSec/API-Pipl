from piplAPI import PiplAPI

# verbose mode
res = PiplAPI({'verbose': True}).get_info('Steve Wozniak')
print res  # retrieves the results

# non verbose mode
res = PiplAPI().get_info('Steve Wozniak')
print res  # retrieves the results
