import cPickle as pickle
class Bird(object):
    have_feather = True
    way_of_reproduction = 'ogg'

summer = Bird()
'''picklestring = pickle.dumps(summer)
print picklestring'''
fn = 'a.pkl'
with open(fn,'r') as f:
    summer = pickle.load(f)
    
print summer
