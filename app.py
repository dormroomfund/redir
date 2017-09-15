from flask import Flask, request, redirect
from collections import defaultdict

SERVER_NAME = 'drf.vc'
REDIRS = defaultdict(lambda: 'https://{}'.format(SERVER_NAME), {
  'join': 'https://medium.com/@dormroomfund/join-the-dorm-room-fund-team-9a01f8326401',
  'join-eng': 'https://medium.com/@yasyf/come-hack-at-dorm-room-fund-4a38bbe8354c'
})

app = Flask(__name__)
app.config['SERVER_NAME'] = SERVER_NAME

@app.route('/')
def redir():
  subdomain = request.host[:-len(SERVER_NAME)].rstrip('.')
  return redirect(REDIRS[subdomain], code=301)
