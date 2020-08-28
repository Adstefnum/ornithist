import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import random
import pickle
from keras.utils import  to_categorical

BASE_DIR = 'C:\\datasets\\100-bird-species'
CATEGORIES = ['ALBATROSS', 'ALEXANDRINE PARAKEET', 'AMERICAN AVOCET', 'AMERICAN BITTERN', 'AMERICAN COOT', 'AMERICAN GOLDFINCH', 'AMERICAN KESTREL', 'AMERICAN REDSTART', 'ANHINGA', 'ANNAS HUMMINGBIRD', 'BALD EAGLE', 'BALTIMORE ORIOLE', 'BANANAQUIT', 'BAR-TAILED GODWIT', 'BARN OWL', 'BARN SWALLOW', 'BAY-BREASTED WARBLER', 'BELTED KINGFISHER', 'BIRD OF PARADISE', 'BLACK FRANCOLIN', 'BLACK SKIMMER', 'BLACK SWAN', 'BLACK-CAPPED CHICKADEE', 'BLACK-NECKED GREBE', 'BLACKBURNIAM WARBLER', 'BLUE HERON', 'BOBOLINK', 'BROWN THRASHER', 'CACTUS WREN', 'CALIFORNIA CONDOR', 'CALIFORNIA GULL', 'CALIFORNIA QUAIL', 'CAPE MAY WARBLER', 'CHARA DE COLLAR', 'CHIPPING SPARROW', 'CINNAMON TEAL', 'COCK OF THE  ROCK', 'COCKATOO', 'COMMON GRACKLE', 'COMMON LOON', 'COMMON POORWILL', 'COMMON STARLING', 'COUCHS KINGBIRD', 'CRESTED AUKLET', 'CRESTED CARACARA', 'CROW', 'CROWNED PIGEON', 'CURL CRESTED ARACURI', 'DARK EYED JUNCO', 'DOWNY WOODPECKER', 'EASTERN BLUEBIRD', 'EASTERN ROSELLA', 'EASTERN TOWEE', 'ELEGANT TROGON', 'EMPEROR PENGUIN', 'EVENING GROSBEAK', 'FLAME TANAGER', 'FLAMINGO', 'FRIGATE', 'GLOSSY IBIS', 'GOLD WING WARBLER', 'GOLDEN CHLOROPHONIA', 'GOLDEN EAGLE', 'GOLDEN PHEASANT', 'GOULDIAN FINCH', 'GRAY CATBIRD', 'GRAY PARTRIDGE', 'GREEN JAY', 'GREY PLOVER', 'HAWAIIAN GOOSE', 'HOODED MERGANSER', 'HOOPOES', 'HOUSE FINCH', 'HOUSE SPARROW', 'HYACINTH MACAW', 'INDIGO BUNTING', 'JABIRU', 'LARK BUNTING', 'LILAC ROLLER', 'LONG-EARED OWL', 'MALLARD DUCK', 'MANDRIN DUCK', 'MARABOU STORK', 'MOURNING DOVE', 'MYNA', 'NICOBAR PIGEON', 'NORTHERN CARDINAL', 'NORTHERN FLICKER', 'NORTHERN GOSHAWK', 'NORTHERN JACANA', 'NORTHERN MOCKINGBIRD', 'NORTHERN RED BISHOP', 'OSPREY', 'OSTRICH', 'PAINTED BUNTIG', 'PARADISE TANAGER', 'PARUS MAJOR', 'PEACOCK', 'PELICAN', 'PEREGRINE FALCON', 'PINK ROBIN', 'PUFFIN', 'PURPLE FINCH', 'PURPLE GALLINULE', 'PURPLE MARTIN', 'PURPLE SWAMPHEN', 'QUETZAL', 'RAINBOW LORIKEET', 'RED FACED CORMORANT', 'RED HEADED WOODPECKER', 'RED THROATED BEE EATER', 'RED WINGED BLACKBIRD', 'RED WISKERED BULBUL', 'RING-NECKED PHEASANT', 'ROADRUNNER', 'ROBIN', 'ROSY FACED LOVEBIRD', 'ROUGH LEG BUZZARD', 'RUBY THROATED HUMMINGBIRD', 'SAND MARTIN', 'SCARLET IBIS', 'SCARLET MACAW', 'SNOWY EGRET', 'SPLENDID WREN', 'STORK BILLED KINGFISHER', 'STRAWBERRY FINCH', 'TEAL DUCK', 'TIT MOUSE', 'TOUCHAN', 'TRUMPTER SWAN', 'TURKEY VULTURE', 'TURQUOISE MOTMOT', 'VARIED THRUSH', 'VENEZUELIAN TROUPIAL', 'VERMILION FLYCATHER', 'VIOLET GREEN SWALLOW', 'WESTERN MEADOWLARK', 'WILSONS BIRD OF PARADISE', 'WOOD DUCK', 'YELLOW HEADED BLACKBIRD']
IMG_SIZE = 50

#returns a 50X50 image and a number label
def get_and_preprocess_data(SUB_DIR,IMG_SIZE=50):
	FULL_DIR = BASE_DIR+'\\'+SUB_DIR
	data = []
	for category in CATEGORIES:
		class_num = (CATEGORIES.index(category)+1)/141 #to ensure working well with model
		path = os.path.join(FULL_DIR,category)

		#In case of a bad image
		for image in os.listdir(path):
			try:
				img_array = cv2.imread(os.path.join(path,image),cv2.IMREAD_GRAYSCALE)
				#new_array = cv2.resize(img_array,(IMG_SIZE,IMG_SIZE))
				data.append([img_array,class_num])
			except Exception as e:
				print(e)
				pass
			'''
			#show one of the images
			plt.imshow(new_array,cmap='gray')
			plt.show()
			break
		break'''
	return data


def final_processing(data,name_x,name_y):
	X= []
	y =[]

	for features,labels in data:
		X.append(features)
		y.append(labels)

	#X = np.array(X).reshape(-1,IMG_SIZE,IMG_SIZE,1)

	#saving current state of dataset to prevent constant reloading
	pickle_out = open(f'{name_x}.pickle','wb')
	pickle.dump(X,pickle_out)
	pickle_out.close()

	pickle_out = open(f'{name_y}.pickle','wb')
	pickle.dump(y,pickle_out)
	pickle_out.close()

#also make sure that all categories have the same number of items because if one greatly 
#outweights the other, it will cause a decision error(It will favor the category that is more)

#shuffle it so the network doesn't read one type of 
#data first then another and so learn wrongly

train = get_and_preprocess_data('train')
random.shuffle(train)
final_processing(train,'X','y')


test = get_and_preprocess_data('test')
random.shuffle(test)

final_processing(test,'test_X','test_y')

