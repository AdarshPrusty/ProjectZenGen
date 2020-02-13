"""word_people_sing: ['man', 'woman', 'boy', 'girl', 'child', 'baby', 'idiot', 'genius', 'fool', 'friend', 'enemy'],
word_places: ['bed', 'tree', 'mountain', 'sea', 'home', 'field', 'stream', 'cliff', 'heaven', 'hell', 'underworld', 'hill', 'sky', 'ditch'],
word_elements: ['heaven', 'earth', 'wind', 'fire', 'water', 'lightning', 'divine', 'shadow', 'storm', ],
word_body_parts: ['mind', 'heart', 'lungs', 'veins', 'aorta', 'foot', 'hand', 'chest', 'eye', 'tongue', 'lips', 'hip', 'nostril', 'hair'],
word_emotions: ['hate', 'love', 'anger', 'calm', 'fear', 'joy', 'sorrow', 'surprise'],
word_time: ['day', 'dawn', 'dusk', 'twilight', 'night', 'evening', 'noon', 'afternoon', 'midnight'],
word_way: ['way', 'path', 'journey', 'destiny', 'route', 'road'],
word_maybe: ['maybe', 'perhaps', 'mayhap', 'possibly'],
word_all: ['man', 'woman', 'boy', 'girl', 'bed', 'tree', 'mountain', 'sea', 'home', 'field', 'heaven', 'earth', 'wind', 'fire', 'water', 'lightning', 'divine', 'mind', 'heart', 'lungs', 'veins', 'aorta', 'foot', 'hand', 'chest', 'eye', 'tongue', 'lips', 'hip', 'nostril', 'hair', 'hate', 'love', 'anger', 'calm', 'disgust', 'fear', 'joy', 'sorrow', 'surprise', 'day', 'dawn', 'dusk', 'twilight', 'night', 'evening', 'noon', 'afternoon', 'midnight', 'way', 'path', 'journey', 'destiny', 'route', 'road','desire', 'rat', 'paper', 'arm', 'poison', 'love', 'prose', 'children', 'heat', 'idea', 'rain', 'legs', 'beef', 'shade', 'drop', 'tail', 'reason', 'control', 'song', 'riddle', 'bone', 'driving', 'work', 'dogs', 'stitch', 'burst', 'story', 'swim', 'quill', 'mountain', 'air', 'cows', 'hot', 'low', 'title', 'hole', 'quince', 'bear', 'knot', 'pull', 'chickens', 'giants', 'weight', 'person', 'afternoon', 'whistle', 'class', 'line', 'move','boat', 'mouth', 'pet', 'night', 'gold', 'chin', 'honey', 'match', 'distance', 'shake', 'wren', 'plants', 'offer', 'authority', 'thing', 'cobweb', 'circle', 'shame', 'sidewalk', 'trees', 'mist', 'shape', 'regret', 'hate', 'rings', 'wine', 'stomach', 'color', 'birds', 'route', 'sun', 'tree', 'voyage', 'twist', 'root', 'lake', 'anger', 'invention', 'ship', 'noise', 'songs', 'battle', 'discovery', 'mask', 'belief', 'flesh', 'hill', 'cup', 'horse', 'ear', 'position', 'loss']
"""

uinp = "word_all: ['man', 'woman', 'boy', 'girl', 'bed', 'tree', 'mountain', 'sea', 'home', 'field', 'heaven', 'earth', 'wind', 'fire', 'water', 'lightning', 'divine', 'mind', 'heart', 'lungs', 'veins', 'aorta', 'foot', 'hand', 'chest', 'eye', 'tongue', 'lips', 'hip', 'nostril', 'hair', 'hate', 'love', 'anger', 'calm', 'disgust', 'fear', 'joy', 'sorrow', 'surprise', 'day', 'dawn', 'dusk', 'twilight', 'night', 'evening', 'noon', 'afternoon', 'midnight', 'way', 'path', 'journey', 'destiny', 'route', 'road','desire', 'rat', 'paper', 'arm', 'poison', 'love', 'prose', 'children', 'heat', 'idea', 'rain', 'legs', 'beef', 'shade', 'drop', 'tail', 'reason', 'control', 'song', 'riddle', 'bone', 'driving', 'work', 'dogs', 'stitch', 'burst', 'story', 'swim', 'quill', 'mountain', 'air', 'cows', 'hot', 'low', 'title', 'hole', 'quince', 'bear', 'knot', 'pull', 'chickens', 'giants', 'weight', 'person', 'afternoon', 'whistle', 'class', 'line', 'move','boat', 'mouth', 'pet', 'night', 'gold', 'chin', 'honey', 'match', 'distance', 'shake', 'wren', 'plants', 'offer', 'authority', 'thing', 'cobweb', 'circle', 'shame', 'sidewalk', 'trees', 'mist', 'shape', 'regret', 'hate', 'rings', 'wine', 'stomach', 'color', 'birds', 'route', 'sun', 'tree', 'voyage', 'twist', 'root', 'lake', 'anger', 'invention', 'ship', 'noise', 'songs', 'battle', 'discovery', 'mask', 'belief', 'flesh', 'hill', 'cup', 'horse', 'ear', 'position', 'loss']"

tei=[]
for i in uinp:
    tei.append(i)

yet=[]
for i in range(len(uinp)):

    if tei[i] == "'" and tei[i-1] == " ":
        yet.append("word: '")
    else:
        yet.append(tei[i])

print ("".join(yet))


"""
word_people_sing: [word: 'man', word: 'woman', word: 'boy', word: 'girl', word: 'child', word: 'baby', word: 'idiot', word: 'genius', word: 'fool', word: 'friend', word: 'enemy'],
word_places: [word: 'bed', word: 'tree', word: 'mountain', word: 'sea', word: 'home', word: 'field', word: 'stream', word: 'cliff', word: 'heaven', word: 'hell', word: 'underworld', word: 'hill', word: 'sky', word: 'ditch'],
word_elements: [word: 'heaven', word: 'earth', word: 'wind', word: 'fire', word: 'water', word: 'lightning', word: 'divine', word: 'shadow', word: 'storm'],
word_body_parts: [word: 'mind', word: 'heart', word: 'lungs', word: 'veins', word: 'aorta', word: 'foot', word: 'hand', word: 'chest', word: 'eye', word: 'tongue', word: 'lips', word: 'hip', word: 'nostril', word: 'hair'],
word_emotions: [word: 'hate', word: 'love', word: 'anger', word: 'calm', word: 'fear', word: 'joy', word: 'sorrow', word: 'surprise'],
word_time: [word: 'day', word: 'dawn', word: 'dusk', word: 'twilight', word: 'night', word: 'evening', word: 'noon', word: 'afternoon', word: 'midnight'],
word_way: [word: 'way', word: 'path', word: 'journey', word: 'destiny', word: 'route', word: 'road'],
word_maybe: [word: 'maybe', word: 'perhaps', word: 'mayhap', word: 'possibly'],
word_all: [word: 'man', word: 'woman', word: 'boy', word: 'girl', word: 'bed', word: 'tree', word: 'mountain', word: 'sea', word: 'home', word: 'field', word: 'heaven', word: 'earth', word: 'wind', word: 'fire', word: 'water', word: 'lightning', word: 'divine', word: 'mind', word: 'heart', word: 'lungs', word: 'veins', word: 'aorta', word: 'foot', word: 'hand', word: 'chest', word: 'eye', word: 'tongue', word: 'lips', word: 'hip', word: 'nostril', word: 'hair', word: 'hate', word: 'love', word: 'anger', word: 'calm', word: 'disgust', word: 'fear', word: 'joy', word: 'sorrow', word: 'surprise', word: 'day', word: 'dawn', word: 'dusk', word: 'twilight', word: 'night', word: 'evening', word: 'noon', word: 'afternoon', word: 'midnight', word: 'way', word: 'path', word: 'journey', word: 'destiny', word: 'route', word: 'road','desire', word: 'rat', word: 'paper', word: 'arm', word: 'poison', word: 'love', word: 'prose', word: 'children', word: 'heat', word: 'idea', word: 'rain', word: 'legs', word: 'beef', word: 'shade', word: 'drop', word: 'tail', word: 'reason', word: 'control', word: 'song', word: 'riddle', word: 'bone', word: 'driving', word: 'work', word: 'dogs', word: 'stitch', word: 'burst', word: 'story', word: 'swim', word: 'quill', word: 'mountain', word: 'air', word: 'cows', word: 'hot', word: 'low', word: 'title', word: 'hole', word: 'quince', word: 'bear', word: 'knot', word: 'pull', word: 'chickens', word: 'giants', word: 'weight', word: 'person', word: 'afternoon', word: 'whistle', word: 'class', word: 'line', word: 'move','boat', word: 'mouth', word: 'pet', word: 'night', word: 'gold', word: 'chin', word: 'honey', word: 'match', word: 'distance', word: 'shake', word: 'wren', word: 'plants', word: 'offer', word: 'authority', word: 'thing', word: 'cobweb', word: 'circle', word: 'shame', word: 'sidewalk', word: 'trees', word: 'mist', word: 'shape', word: 'regret', word: 'hate', word: 'rings', word: 'wine', word: 'stomach', word: 'color', word: 'birds', word: 'route', word: 'sun', word: 'tree', word: 'voyage', word: 'twist', word: 'root', word: 'lake', word: 'anger', word: 'invention', word: 'ship', word: 'noise', word: 'songs', word: 'battle', word: 'discovery', word: 'mask', word: 'belief', word: 'flesh', word: 'hill', word: 'cup', word: 'horse', word: 'ear', word: 'position', word: 'loss']
"""