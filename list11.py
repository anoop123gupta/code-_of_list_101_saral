## -------part1------------
question_list = ["1.How many continents are there?","2.What is the capital of India?","3.NG mei kaun se course padhaya jaata hai?"]
options_list = [
				["1.Four", "2.Nine", "3.Seven", "4.Eight"],	
				["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],
				["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]]
solution_list = [3, 4, 1]
# ------part2--------print all questions and corresponding options -----
# for i in range(len(question_list)):
# 	print question_list[i]
# 	for j in options_list[i]:    
# 		print j
# ------------------------------------------------
# print "apka sawal ye raha : "
# print question_list[1]
# print "\n"
# print "apke options ye rahe :"

# for j in options_list[1]:
# 	print j    
# ------------------------------------------------
# for i in range(len(question_list)):
# 	print "apka sawal ye raha : "
# 	print question_list[i],'\n'
# 	print "apke options ye rahe :"
# 	for j in options_list[i]:   
# 		print j
# 	print '' 
# --------------------------------------------------------
for i in range(len(question_list)):
	print "apka sawal ye raha : "
	print question_list[i],'\n'
	print "apke options ye rahe :"
	for j in options_list[i]:   
		print j
	user=int(raw_input("enter your answer "))
	if user==solution_list[i]:
		print "congrates! sahi jawab \n"
	elif user==5050:
		
	else:
		print "apne galat jawab diya h isliye apko game se  bahar kar diya gaya hai "
		break
