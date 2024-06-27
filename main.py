from bs4 import BeautifulSoup 

with open("home.html","r") as html_file:
    content=html_file.read()
    
    soup=BeautifulSoup(content,"lxml")
      #for printing courses


    #courses=soup.find('h5')
    #courses=soup.find_all("h5")
    #for course in courses:
    #    print(course.text)
    

    course_cards=soup.find_all('div',class_='card')
    for course in course_cards:
     course_name=course.h5.text
     course_price=course.a.text
     print(course_name+" costs"+course_price.split()[-1])


