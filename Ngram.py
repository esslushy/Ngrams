import codecs
import collections
import re
text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer tincidunt, augue vitae rhoncus sagittis, lectus tellus imperdiet risus, et dapibus quam sapien nec augue. Suspendisse tellus turpis, vestibulum vel massa quis, rhoncus porta ante. Nunc dictum molestie consequat. Vestibulum fringilla nec diam in cursus. Nulla sit amet blandit sem, ut gravida risus. Cras vitae erat mattis, dapibus neque eget, sagittis orci. Pellentesque ligula metus, aliquet et imperdiet in, laoreet vel sem. Curabitur at justo at leo pulvinar elementum. Maecenas tristique nulla quis eros mattis condimentum. Donec dolor lorem, faucibus sed justo at, venenatis venenatis nisi. Aenean cursus rutrum volutpat. Integer rutrum mattis urna, ac pellentesque purus porta quis. Quisque rhoncus vestibulum aliquet. Maecenas id purus ex. Vestibulum nec pulvinar nisl. Proin vulputate ipsum ligula, vestibulum feugiat nulla pellentesque ut. Suspendisse ut metus quis lectus luctus imperdiet. Vestibulum eu augue elementum urna facilisis ultrices egestas id arcu. Sed mollis laoreet leo, facilisis cursus nulla aliquam nec. Quisque porta elit et felis sagittis fermentum. Aliquam efficitur vestibulum nisi. Aliquam vel sollicitudin turpis. Cras congue, metus in condimentum cursus, massa velit tincidunt turpis, ac lobortis quam nulla sit amet sem. Cras in lectus eu dolor placerat imperdiet quis sed ante. Maecenas mollis tempor purus ultricies imperdiet. Ut in euismod arcu, id vestibulum nibh. Pellentesque ac est in mi scelerisque dignissim sit amet non urna. Etiam sed sagittis nisi, ac sagittis arcu. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris eget ornare quam, quis vulputate sapien. Pellentesque malesuada felis justo, non congue nunc fringilla eu. Cras pellentesque porttitor placerat. Nulla hendrerit tempus ipsum, a iaculis nulla. Sed eget dui eu purus mattis interdum id eget ligula. Donec sagittis nibh massa, quis ultricies turpis aliquet et. Sed sed convallis enim. Nullam fringilla consectetur velit, et auctor neque. Ut gravida, urna ut luctus eleifend, orci nulla ornare enim, id dapibus erat leo ut metus. Praesent euismod fringilla leo a feugiat. Aenean lorem justo, sodales at sodales eget, efficitur non mauris. Morbi elementum orci nisi, a varius orci mollis vitae. Quisque tempor malesuada justo sit amet condimentum. Cras aliquam eu eros et fermentum. Suspendisse commodo convallis nisi nec sollicitudin. Vestibulum placerat ex ac placerat volutpat. Ut suscipit molestie vulputate. In feugiat molestie varius. Vestibulum facilisis, est ac fermentum porta, augue justo ultrices felis, non convallis erat urna eget risus. Praesent vitae laoreet odio. Phasellus vestibulum blandit convallis. Maecenas at erat eu metus facilisis fringilla. Nulla vulputate, ligula ac vestibulum lobortis, metus dolor commodo nibh, a faucibus lectus ipsum ac felis. Maecenas sed malesuada neque, eu commodo purus. Phasellus quis consectetur odio. In at eros sed tellus suscipit mattis. Maecenas rutrum consequat auctor. Phasellus ultricies fermentum risus, id rhoncus sapien ultricies ac. Sed id orci accumsan, eleifend magna quis, fringilla est. Sed tempus tempor accumsan. Donec euismod, odio sed sollicitudin convallis, purus nibh porttitor risus, a lacinia nulla mauris sed diam. Integer vitae justo sed libero lobortis consequat. Integer eu sodales ligula. Nulla facilisi. Fusce eget hendrerit sem. Nunc feugiat nisl id blandit feugiat."
print("content_string")
file_object = codecs.open('text.txt', 'r', encoding='utf8', errors='ignore')

content_string = file_object.read()

file_object.close()
translate = ",.;:?!()*_-+=" + '"'
Arraystring = content_string.split()
for i in range(0, len(Arraystring)):
	Arraystring[i] = re.sub("[^a-zA-Z]+", "", Arraystring[i])

print (collections.Counter(Arraystring))

#digram array
digrams = []
for x in range(0, len(Arraystring) - 1):
	digrams.append(Arraystring[x] + " " + Arraystring[x+1])

print(collections.Counter(digrams))

trigrams = []
for z in range(0, len(Arraystring) - 2):
	trigrams.append(Arraystring[z] + " " + Arraystring[z+1] + " " + Arraystring[z+2])

print(collections.Counter(trigrams))