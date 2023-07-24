{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "d277933a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Have a Good Day!\n"
     ]
    }
   ],
   "source": [
    "alien_color='Blue'\n",
    "if alien_color=='green':\n",
    "    print(\"You just won 5 points!!\")\n",
    "elif alien_color=='yellow':\n",
    "    print(\"You just won 10 points!!\")\n",
    "elif alien_color=='red':\n",
    "    print(\"You just won 15 points!!\")\n",
    "    \n",
    "print(\"Have a Good Day!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "31c02904",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Person is a elder!\n"
     ]
    }
   ],
   "source": [
    "age= 100\n",
    "\n",
    "if age <2:\n",
    "    print(\"Person is a baby!\")\n",
    "elif age <4:\n",
    "    print(\"Person is a Toddler!\")\n",
    "elif age <13:\n",
    "    print(\"Person is a kid!\")\n",
    "elif age >= 13 and age < 20:\n",
    "    print(\"Person is a teenager!\")\n",
    "elif age <65:\n",
    "    print(\"Person is a adult!\")\n",
    "else:\n",
    "    print(\"Person is a elder!\")\n",
    "    \n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "aa6d3dfe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Yes\n"
     ]
    }
   ],
   "source": [
    "\n",
    "fruit=['ban','man','app']\n",
    "\n",
    "if 'app' in fruit:\n",
    "    print('Yes')\n",
    "else:\n",
    "    print('No')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "3b183025",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Added topping Mushrooms\n",
      "Sorry we are out of Green Peppers\n",
      "Added topping Extra Cheese\n",
      "\n",
      "Finished making your pizza!\n"
     ]
    }
   ],
   "source": [
    "requested_Toppings=['Mushrooms','Green Peppers','Extra Cheese']\n",
    "\n",
    "if requested_Toppings:\n",
    "    for requested_Topping in requested_Toppings:\n",
    "        if requested_Topping=='Green Peppers':\n",
    "            print(f\"Sorry we are out of {requested_Topping}\")\n",
    "        else:\n",
    "            print(f\"Added topping {requested_Topping}\")\n",
    "    print(\"\\nFinished making your pizza!\")\n",
    "else:\n",
    "    print(\"Are you sure you want a plain pizza?\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "ad146cd4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Added Toppings Mushrooms\n",
      "Added Toppings Green Peppers\n",
      "Sorry French Fries is not available\n",
      "Added Toppings Extra Cheese\n",
      "\n",
      "Finished making your pizza!\n"
     ]
    }
   ],
   "source": [
    "available_Toppings=['Mushrooms','olives','pineapple','pepperoni','Green Peppers','Extra Cheese']\n",
    "requested_Toppings=['Mushrooms','Green Peppers','French Fries','Extra Cheese']\n",
    "\n",
    "for requested_Topping in requested_Toppings:\n",
    "    if requested_Topping in available_Toppings:\n",
    "        print(f\"Added Toppings {requested_Topping}\")\n",
    "    else:\n",
    "        print(f\"Sorry {requested_Topping} is not available\")\n",
    "\n",
    "print(\"\\nFinished making your pizza!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "c21d9d63",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello admin, would you lke to see a status report?\n",
      " Welcome nis, Thankyou for logging in!\n",
      " Welcome kai, Thankyou for logging in!\n",
      " Welcome rak, Thankyou for logging in!\n",
      " Welcome may, Thankyou for logging in!\n",
      " Welcome abhi, Thankyou for logging in!\n",
      " Welcome nav, Thankyou for logging in!\n",
      " Welcome niya, Thankyou for logging in!\n",
      " Welcome saag, Thankyou for logging in!\n"
     ]
    }
   ],
   "source": [
    "user_names=['admin','nis','kai','rak','may','abhi','nav','niya','saag']\n",
    "\n",
    "for user_name in user_names:\n",
    "    if user_name=='admin':\n",
    "        print(\"Hello admin, would you lke to see a status report?\")\n",
    "    else:\n",
    "        print(f\" Welcome {user_name}, Thankyou for logging in!\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "d1fbf519",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "No Users!!\n"
     ]
    }
   ],
   "source": [
    "user_names=[]\n",
    "\n",
    "if user_names:\n",
    "    for user_name in user_names:\n",
    "        if user_name=='admin':\n",
    "            print(\"Hello admin, would you lke to see a status report?\")\n",
    "        else:\n",
    "            print(f\" Welcome {user_name}, Thankyou for logging in!\")\n",
    "else:\n",
    "    print(\"No Users!!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "2720d45b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "abhi is already being used, enter new user name.\n",
      "nav is already being used, enter new user name.\n",
      "user name niya is available\n",
      "user name saag is available\n"
     ]
    }
   ],
   "source": [
    "current_users=['admin','nis','kai','rak','may','Abhi','nav']\n",
    "new_users=['abhi','nav','niya','saag']\n",
    "\n",
    "current_users_lower=[user.lower() for user in current_users]\n",
    "\n",
    "for new_user in new_users:\n",
    "    if new_user.lower() in current_users_lower:\n",
    "        print(f\"{new_user} is already being used, enter new user name.\")\n",
    "    else:\n",
    "        print(f\"user name {new_user} is available\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "d5fc87fd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 5, 6, 7, 8, 9]\n"
     ]
    }
   ],
   "source": [
    "numbers = list(range(1,10))\n",
    "print(numbers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "73338a1b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n"
     ]
    }
   ],
   "source": [
    "alien_0={'x_pos':0,'y_pos':'20','pace':'medium'}\n",
    "\n",
    "# Move alien to right\n",
    "\n",
    "if alien_0['pace']=='slow':\n",
    "    alien_0['x_pos']= alien_0['x_pos']+ 1\n",
    "    \n",
    "elif alien_0['pace']=='medium':\n",
    "    alien_0['x_pos']= alien_0['x_pos']+ 2\n",
    "    \n",
    "elif alien_0['pace']=='Fast':\n",
    "    alien_0['x_pos']= alien_0['x_pos']+ 3\n",
    "    \n",
    "print(alien_0['x_pos'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "8b1f99e4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " Nis's fav number is 789957 \n"
     ]
    }
   ],
   "source": [
    "phone_dic={\n",
    "    'nis':'789957',\n",
    "    'rak':'456210',\n",
    "    'may':'789562',\n",
    "}\n",
    "\n",
    "print(f\" Nis's fav number is {phone_dic['nis']} \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "b575bb01",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "nis joined the poll!\n",
      "phil, I see you love c \n",
      "sarah, I see you love python \n"
     ]
    }
   ],
   "source": [
    "fav_language={\n",
    "    'phil':'c',\n",
    "    'nis':'c++',\n",
    "    'sarah':'python'\n",
    "    }\n",
    "\n",
    "friends=['phil','sarah']\n",
    "for name in sorted(fav_language.keys()):\n",
    "    if name in friends:\n",
    "        lang=fav_language[name]\n",
    "        print(f\"{name}, I see you love {lang} \")\n",
    "    else:\n",
    "        print(f\"{name} joined the poll!\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "08005c9e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Nile flows in country Egypt !\n",
      "Amazon flows in country Brazil !\n",
      "Ganga flows in country India !\n"
     ]
    }
   ],
   "source": [
    "river_dic={'nile':'egypt','Amazon':'Brazil','Ganga':'India'}\n",
    "\n",
    "for key, value in river_dic.items():\n",
    "    print(f\"{key.title()} flows in country {value.title()} !\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "e1c38a0b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "egypt\n",
      "Brazil\n",
      "India\n"
     ]
    }
   ],
   "source": [
    "river_dic={'nile':'egypt','Amazon':'Brazil','Ganga':'India'}\n",
    "\n",
    "for key, value in river_dic.items():\n",
    "    print(value)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "4b6db4c6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "nis, loves language python\n",
      "may, loves language C\n",
      "kai, loves language C++\n",
      "rak, loves language java\n",
      "saag, please take the poll!\n",
      "nav, please take the poll!\n",
      "These are the poll results!\n"
     ]
    }
   ],
   "source": [
    "fav_lang={\n",
    "    'nis':'python',\n",
    "    'may':'C',\n",
    "    'kai':'C++',\n",
    "    'rak':'java'\n",
    "    }\n",
    "\n",
    "list=['nis','may','kai','rak','saag','nav']\n",
    "\n",
    "for name in list:\n",
    "    if name not in fav_lang.keys():\n",
    "        print(f\"{name}, please take the poll!\")\n",
    "    else:\n",
    "        print(f\"{name}, loves language {fav_lang[name]}\")\n",
    "\n",
    "print(\"These are the poll results!\")\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "dd838e4f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "[{'color': 'green', 'points': 5, 'speed': 'slow'}, {'color': 'green', 'points': 5, 'speed': 'slow'}, {'color': 'green', 'points': 5, 'speed': 'slow'}, {'color': 'green', 'points': 5, 'speed': 'slow'}, {'color': 'green', 'points': 5, 'speed': 'slow'}]\n",
      "Total number of aliens: 30\n"
     ]
    }
   ],
   "source": [
    "aliens=[]\n",
    "\n",
    "for alien in range(30):\n",
    "    new_alien={'color':'green','points':5,'speed':'slow'}\n",
    "    aliens.append(new_alien)\n",
    "\n",
    "#show the first five aliens\n",
    "print(f\"\\n{aliens[:5]}\")\n",
    "\n",
    "#show how many aliens have been created\n",
    "print(f\"Total number of aliens: {len(aliens)}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "fbaced76",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "First five aliens:[{'color': 'yellow', 'points': 10, 'speed': 'medium'}, {'color': 'yellow', 'points': 10, 'speed': 'medium'}, {'color': 'yellow', 'points': 10, 'speed': 'medium'}, {'color': 'green', 'points': 5, 'speed': 'slow'}, {'color': 'green', 'points': 5, 'speed': 'slow'}]\n"
     ]
    }
   ],
   "source": [
    "aliens=[]\n",
    "\n",
    "for alien in range(30):\n",
    "    new_alien={'color':'green','points':5,'speed':'slow'}\n",
    "    aliens.append(new_alien)\n",
    "    \n",
    "# change first 2 aliens to yellow, medium, 10.\n",
    "\n",
    "for alien in aliens[:3]:\n",
    "    if alien['color']=='green':\n",
    "        alien['color']='yellow'\n",
    "        alien['points']=10\n",
    "        alien['speed']='medium'\n",
    "        \n",
    "print(f\"First five aliens:{aliens[:5]}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "157f08c1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "nis loves language\n",
      "\t python\n",
      "\t c\n",
      "\n",
      "rak loves language\n",
      "\t c\n",
      "\t c++\n",
      "\n",
      "niya loves language\n",
      "\t java\n",
      "\t R\n"
     ]
    }
   ],
   "source": [
    "fav_lan={\n",
    "    'nis':['python','c'],\n",
    "    'rak':['c','c++'],\n",
    "    'niya':['java','R']\n",
    "}\n",
    "for name, lang in fav_lan.items():\n",
    "    print(f\"\\n{name} loves language\")\n",
    "    for lan in lang:\n",
    "        print(f\"\\t {lan}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "294f5c44",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "User Name is :aeinstein\n",
      "\t Full Name: albert einstein\n",
      "\t Lacation : princeton\n",
      "\n",
      "User Name is :mcurie\n",
      "\t Full Name: marie curie\n",
      "\t Lacation : paris\n",
      "\n"
     ]
    }
   ],
   "source": [
    "user={\n",
    "    'aeinstein':{'first':'albert','last':'einstein','location':'princeton'},\n",
    "     'mcurie':{'first':'marie','last':'curie','location':'paris'}\n",
    "}\n",
    "for username, userinfo in user.items():\n",
    "    print(f\"User Name is :{username}\")\n",
    "    fullname=print(f\"\\t Full Name: {userinfo['first']} {userinfo['last']}\")\n",
    "    location=print(f\"\\t Lacation : {userinfo['location']}\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "87b3fb5c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Name of the city: bangalore\n",
      "\tCountry: india\n",
      "\tPopulation: 100000\n",
      "\tFact: Garden City\n",
      "\n",
      "Name of the city: rome\n",
      "\tCountry: italy\n",
      "\tPopulation: 15000\n",
      "\tFact: Ancient City\n",
      "\n",
      "Name of the city: New York\n",
      "\tCountry: USA\n",
      "\tPopulation: 150000\n",
      "\tFact: Largest City\n"
     ]
    }
   ],
   "source": [
    "city={'bangalore':{'country':'india','population':'100000','fact':'Garden City'},\n",
    "'rome':{'country':'italy','population':'15000','fact':'Ancient City'},\n",
    "'New York':{'country':'USA','population':'150000','fact':'Largest City'}}\n",
    "\n",
    "for name, cityinfo in city.items():\n",
    "    print(f\"\\nName of the city: {name}\")\n",
    "    print(f\"\\tCountry: {cityinfo['country']}\" )\n",
    "    print(f\"\\tPopulation: {cityinfo['population']}\" )\n",
    "    print(f\"\\tFact: {cityinfo['fact']}\" )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aef64b25",
   "metadata": {},
   "outputs": [],
   "source": [
    "name=input(\"What is your name? : \")\n",
    "print(f'the name is {name}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "898233f3",
   "metadata": {},
   "outputs": [],
   "source": [
    "car=input(\"What kind of car would you like to rent? : \")\n",
    "print(f\"Let's see if we can find you a {car}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "40a34f72",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "How many people are in your dining group? : 9\n",
      "Please wait for a table\n"
     ]
    }
   ],
   "source": [
    "people=input(\"How many people are in your dining group? : \")\n",
    "people=int(people)\n",
    "if people>8:\n",
    "    print(f\"Please wait for a table\")\n",
    "else:\n",
    "    print(\"Table is available\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "aa8fbf5f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "We will determine if number is a multiple of 10\n",
      "Please enter a number: 10\n",
      "10 is a  multiple of 10\n"
     ]
    }
   ],
   "source": [
    "num=\"We will determine if number is a multiple of 10\"\n",
    "num+=\"\\nPlease enter a number: \"\n",
    "number=input(num)\n",
    "number=int(number)\n",
    "mod=number%10\n",
    "if mod==0:\n",
    "    print(f'{number} is a  multiple of 10')\n",
    "else:\n",
    "    print(f'{number} is not a multiple of 10')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "d4c48484",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Ada Lovelace\n"
     ]
    }
   ],
   "source": [
    "name=\"ada\"\n",
    "name2=\"lovelace\"\n",
    "print((f\"{name} {name2}\").title())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "d725c261",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ada Lovelace!\n"
     ]
    }
   ],
   "source": [
    "name=\"ada\"\n",
    "name2=\"lovelace\"\n",
    "fullname=\"{} {}!\".format(name,name2.capitalize())\n",
    "print(fullname)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "2d530811",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n"
     ]
    }
   ],
   "source": [
    "x,y,z=0,0,3\n",
    "print(y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "2ef0dc56",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1244\n"
     ]
    }
   ],
   "source": [
    "ASDF=1000\n",
    "asdf='1244'\n",
    "print(asdf)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "422f29e7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "My name is Nis!\n"
     ]
    }
   ],
   "source": [
    "user_names=['admin','nis','kai','rak','may','abhi','nav','niya','saag']\n",
    "message=f\"My name is {user_names[1].title()}!\"\n",
    "print(message)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "549d2750",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "My name is  Nis!\n"
     ]
    }
   ],
   "source": [
    "user_names=['admin','nis','kai','rak','may','abhi','nav','niya','saag']\n",
    "message=\"{} {}!\".format(\"My name is \",user_names[1].title())\n",
    "print(message)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "d61460c9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['admin', 'nis', 'kai', 'rak', 'may', 'abhi', 'nav', 'niya', 'saag', 'var']\n"
     ]
    }
   ],
   "source": [
    "user_names=['admin','nis','kai','rak','may','abhi','nav','niya','saag']\n",
    "user_names.append('var')\n",
    "print(user_names)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "83fa7c86",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['admin', 'nis', 'kai', '123', 'rak', 'may', 'abhi', 'nav', 'niya', 'saag']\n"
     ]
    }
   ],
   "source": [
    "user_names=['admin','nis','kai','rak','may','abhi','nav','niya','saag']\n",
    "user_names.insert(3,'123')\n",
    "print(user_names)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "dfb71a7e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['admin', 'nis', 'rak', 'may', 'abhi', 'nav', 'niya', 'saag']\n"
     ]
    }
   ],
   "source": [
    "user_names=['admin','nis','kai','rak','may','abhi','nav','niya','saag']\n",
    "del user_names[2]\n",
    "print(user_names)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "d184affb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['admin', 'nis', 'kai', 'rak', 'may', 'abhi', 'nav', 'niya']\n",
      "saag\n"
     ]
    }
   ],
   "source": [
    "user_names=['admin','nis','kai','rak','may','abhi','nav','niya','saag']\n",
    "popped_username=user_names.pop()\n",
    "print(user_names)\n",
    "print(popped_username)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "a7005f9f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['saag', 'niya', 'nav', 'abhi', 'may', 'rak', 'kai', 'nis', 'admin']\n"
     ]
    }
   ],
   "source": [
    "user_names=['admin','nis','kai','rak','may','abhi','nav','niya','saag']\n",
    "user_names.reverse()\n",
    "print(user_names)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "4fd9b723",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Admin,is the user\n",
      "Nis,is the user\n",
      "Kai,is the user\n",
      "Rak,is the user\n",
      "May,is the user\n",
      "Abhi,is the user\n",
      "Nav,is the user\n",
      "Niya,is the user\n",
      "Saag,is the user\n"
     ]
    }
   ],
   "source": [
    "user_names=['admin','nis','kai','rak','may','abhi','nav','niya','saag']\n",
    "for user in user_names:\n",
    "    print(f\"{user.title()},is the user\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "1eadc95b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]\n"
     ]
    }
   ],
   "source": [
    "squares=[]\n",
    "for i in range(1,11):\n",
    "    square=i**2\n",
    "    squares.append(square)\n",
    "\n",
    "print(squares)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "779f134c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[]\n"
     ]
    }
   ],
   "source": [
    "squares=[]\n",
    "m=[]\n",
    "for i in range(1,11):\n",
    "    square=i**2\n",
    "    squares.append(square)\n",
    "    squares==m\n",
    "\n",
    "print(m)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "a88a92ef",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "500000500000\n"
     ]
    }
   ],
   "source": [
    "#sum million numbers\n",
    "\n",
    "number=list(range(1,1000001))\n",
    "sum=0\n",
    "for i in number:\n",
    "    sum=sum+i\n",
    "\n",
    "print(sum)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "384b6277",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]\n"
     ]
    }
   ],
   "source": [
    "cubes=[values**3 for values in range(1,11)]\n",
    "print(cubes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "c864f269",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Admin\n",
      "Nis\n",
      "Kai\n",
      "Rak\n"
     ]
    }
   ],
   "source": [
    "user_names=['admin','nis','kai','rak','may','abhi','nav','niya','saag']\n",
    "\n",
    "for names in user_names[0:4]:\n",
    "    print(names.title())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "b6fc4380",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['pizza', 'mango', 'icecream', 'coco']\n",
      "['pizza', 'mango', 'icecream', 'beer']\n"
     ]
    }
   ],
   "source": [
    "my_food=['pizza','mango','icecream']\n",
    "my_friends_food=my_food[:]\n",
    "my_food.append('coco')\n",
    "my_friends_food.append('beer')\n",
    "print(my_food)\n",
    "print(my_friends_food)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "417f86a2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Pizza\n",
      "MANGO\n",
      "Icecream\n"
     ]
    }
   ],
   "source": [
    "my_food=['pizza','mango','icecream']\n",
    "for food in my_food:\n",
    "    if food=='mango':\n",
    "        print(food.upper())\n",
    "    else:\n",
    "        print(food.title())\n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "a901a720",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "False\n"
     ]
    }
   ],
   "source": [
    "my_food=['pizza','mango','icecream']\n",
    "print('pizza' not in my_food)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "f6c6f3d5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "if car == 'honda', I predict true\n",
      "True\n",
      "\n",
      "if car is bmw, I predict true \n",
      "False\n"
     ]
    }
   ],
   "source": [
    "car='honda'\n",
    "\n",
    "print(\"if car == 'honda', I predict true\")\n",
    "print(car=='honda')\n",
    "\n",
    "print(\"\\nif car is bmw, I predict true \")\n",
    "print(car=='bmw')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "7587e5d2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Adding Mshroom.\n"
     ]
    }
   ],
   "source": [
    "toppings=['Mushroom','extra cheese']\n",
    "if 'Mushroom' in toppings:\n",
    "    print(\"Adding Mushroom.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "00fc1e40",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Adding Mushroom.\n"
     ]
    }
   ],
   "source": [
    "toppings=['Mushroom','extra cheese']\n",
    "for top in toppings:\n",
    "    if top=='Mushroom':\n",
    "        print(\"Adding Mushroom.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "c073a92b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Are you sure you want plane pizza?\n"
     ]
    }
   ],
   "source": [
    "toppings=[]\n",
    "if toppings:\n",
    "    for topping in toppings:\n",
    "        print(f\"Adding {topping}\")\n",
    "else:\n",
    "     print(\"Are you sure you want plane pizza?\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "403f5fb6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "green\n"
     ]
    }
   ],
   "source": [
    "alien_0={'colour':'green'}\n",
    "print(alien_0['colour'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "c17324e1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'colour': 'green', 'POINTS': 5}\n",
      "{'colour': 'green', 'POINTS': 5, 'x position': 0, 'y position': 25}\n",
      "x position is Green\n",
      "\n",
      "key:colour\n",
      "Value:green\n",
      "the alien games attributes 'colour' and its values:green\n",
      "\n",
      "key:POINTS\n",
      "Value:5\n",
      "the alien games attributes 'POINTS' and its values:5\n",
      "\n",
      "key:x position\n",
      "Value:0\n",
      "the alien games attributes 'x position' and its values:0\n",
      "\n",
      "key:y position\n",
      "Value:25\n",
      "the alien games attributes 'y position' and its values:25\n",
      "\n",
      "colour\n",
      "\n",
      "POINTS\n",
      "\n",
      "x position\n",
      "\n",
      "y position\n"
     ]
    }
   ],
   "source": [
    "alien_0={'colour':'green','POINTS':5}\n",
    "print(alien_0)\n",
    "\n",
    "#Add new keyvalues\n",
    "alien_0['x position']=0\n",
    "alien_0['y position']=25\n",
    "\n",
    "print(alien_0)\n",
    "\n",
    "print(f\"x position is {alien_0['colour'].title()}\")\n",
    "\n",
    "for key, value in alien_0.items():\n",
    "    print(f\"\\nkey:{key}\")\n",
    "    print(f\"Value:{value}\")\n",
    "    print(f\"the alien games attributes '{key}' and its values:{value}\")\n",
    "    \n",
    "for key in alien_0.keys():\n",
    "    print(f\"\\n{key}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "ae8124fa",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[{'colour': 'green', 'points': '5', 'speed': 'slow'}, {'colour': 'green', 'points': '5', 'speed': 'slow'}, {'colour': 'green', 'points': '5', 'speed': 'slow'}, {'colour': 'green', 'points': '5', 'speed': 'slow'}, {'colour': 'green', 'points': '5', 'speed': 'slow'}]\n",
      "...\n",
      "Total Number of Aliens: 50\n"
     ]
    }
   ],
   "source": [
    "aliens=[]\n",
    "\n",
    "\n",
    "for alien in range(50):\n",
    "    new_alien={'colour': 'green','points':'5', 'speed': 'slow'}\n",
    "    aliens.append(new_alien)\n",
    "print(f\"{aliens[:5]}\")\n",
    "print(f\"...\")\n",
    "\n",
    "print(f\"Total Number of Aliens: {len(aliens)}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "35054e64",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[{'colour': 'red', 'points': '5', 'speed': 'slow'}, {'colour': 'red', 'points': '5', 'speed': 'slow'}, {'colour': 'red', 'points': '5', 'speed': 'slow'}, {'colour': 'Yellow', 'points': '5', 'speed': 'slow'}, {'colour': 'Yellow', 'points': '5', 'speed': 'slow'}]\n",
      "...\n"
     ]
    }
   ],
   "source": [
    "aliens=[]\n",
    "\n",
    "\n",
    "for alien in range(50):\n",
    "    new_alien={'colour': 'green','points':'5', 'speed': 'slow'}\n",
    "    aliens.append(new_alien)\n",
    "\n",
    "for alien in aliens[:5]:\n",
    "    if alien['colour']=='green':\n",
    "        alien['colour']='Yellow'\n",
    "        \n",
    "for alien in aliens[:3]:\n",
    "    if alien['colour']=='Yellow':\n",
    "        alien['colour']='red'\n",
    "\n",
    "print(f\"{aliens[:5]}\")\n",
    "print(f\"...\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f5aad4e8",
   "metadata": {},
   "source": [
    " aliens=[]\n",
    "\n",
    "\n",
    "for alien in range(50):\n",
    "    new_alien={'colour': 'green','points':'5', 'speed': 'slow'}\n",
    "    aliens.append(new_alien)\n",
    "    \n",
    "\n",
    "for alien in aliens[:3]:\n",
    "    print(f\"{alien}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "f7346d50",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "you ordered a thick crust pizza with following toppings:\n",
      "cheese\n",
      "meat\n",
      "egg\n"
     ]
    }
   ],
   "source": [
    "pizza ={'crust':'thick','toppings':['cheese','meat','egg']}\n",
    "\n",
    "print(f\"you ordered a {pizza['crust']} crust pizza with following toppings:\")\n",
    " \n",
    "for i in pizza['toppings']:\n",
    "        print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "3eb8cd2b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Jen\n",
      "\tAssc\n",
      "\tA\n",
      "\n",
      "Ken\n",
      "\tB\n",
      "\tF\n",
      "\n",
      "Ben\n",
      "\tR\n",
      "\tY\n",
      "\tQ\n"
     ]
    }
   ],
   "source": [
    "fav_lan={'jen':['assc','a'],'ken':['b','f'],'ben':['r','y','q']}\n",
    "\n",
    "for name,lan in fav_lan.items():\n",
    "    print(f\"\\n{name.title()}\")\n",
    "    for values in lan[:]:\n",
    "        print(f\"\\t{values.title()}\")\n",
    "   \n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "ea6bc73c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "If you tell us who we are, we can personalize your experience\n",
      " What is your first name?Nishith\n",
      " Hello, Nishith\n"
     ]
    }
   ],
   "source": [
    "prompt=\"If you tell us who we are, we can personalize your experience\"\n",
    "prompt+=\"\\n What is your first name?\"\n",
    "\n",
    "Message = input(prompt)\n",
    "\n",
    "print(f\" Hello, {Message}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "e5e10eb6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "What is your age?: 34\n",
      "Adult\n",
      "Have a goof day!\n"
     ]
    }
   ],
   "source": [
    "age=input(\"What is your age?: \")\n",
    "\n",
    "age=int(age)\n",
    "\n",
    "if age>18:\n",
    "    print(\"Adult\")\n",
    "else:\n",
    "    print(\"Kid\")\n",
    "\n",
    "print(\"Have a goof day!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "f82cd6d8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "current_number=1\n",
    "while current_number<=5:\n",
    "    print(current_number)\n",
    "    current_number+=1\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "dda66f40",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "If you tell us who we are, we can personalize your experience\n",
      " What is your first name?QUIT\n",
      "Quit\n"
     ]
    }
   ],
   "source": [
    "message=\"\"\n",
    "\n",
    "while message!=\"Quit\":\n",
    "    message= input(prompt).title()\n",
    "    print(message)\n",
    "   \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "a491dda6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "bjioo\n",
      "bjioo\n"
     ]
    }
   ],
   "source": [
    "message = input()\n",
    "print(message)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "1d921f15",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "asdf\n",
      "asdf\n",
      "Quit\n",
      "Quit\n"
     ]
    }
   ],
   "source": [
    "message =\"\"\n",
    "while message !=\"Quit\":\n",
    "    message=input()\n",
    "    print(message)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "70c61b79",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "nnnn\n",
      "Nnnn\n",
      "quit\n",
      "Quit\n"
     ]
    }
   ],
   "source": [
    "prompt = \"\\nTell me something and I'll repeat\"\n",
    "prompt+= \"\\nEnter 'Quit' to quit the program\"\n",
    "\n",
    "message=\"\"\n",
    "\n",
    "while message!=\"Quit\":\n",
    "    message= input().title()\n",
    "    print(message)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "cf29a80d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Tell me something and I'll repeat\n",
      "Enter 'Quit' to quit the programasd\n",
      "Asd\n",
      "\n",
      "Tell me something and I'll repeat\n",
      "Enter 'Quit' to quit the programquit\n"
     ]
    }
   ],
   "source": [
    "prompt = \"\\nTell me something and I'll repeat\"\n",
    "prompt+= \"\\nEnter 'Quit' to quit the program\"\n",
    "\n",
    "message=\"\"\n",
    "Active = True\n",
    "while message!=\"Quit\":\n",
    "    message=input(prompt).title()\n",
    "    \n",
    "    if message==\"Quit\":\n",
    "        Active= False\n",
    "    else:\n",
    "        print(message)\n",
    "        \n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "fc341b97",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Tell me something and I'll repeat\n",
      "Enter 'Quit' to quit the programasdf\n",
      "Asdf\n",
      "\n",
      "Tell me something and I'll repeat\n",
      "Enter 'Quit' to quit the programquit\n"
     ]
    }
   ],
   "source": [
    "prompt = \"\\nTell me something and I'll repeat\"\n",
    "prompt+= \"\\nEnter 'Quit' to quit the program\"\n",
    "\n",
    "Active = True\n",
    "while Active:\n",
    "    message=input(prompt).title()\n",
    "    \n",
    "    if message==\"Quit\":\n",
    "        Active= False\n",
    "    else:\n",
    "        print(message)\n",
    "        \n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "b18eb1d2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "3\n",
      "5\n",
      "7\n",
      "9\n"
     ]
    }
   ],
   "source": [
    "number=0\n",
    "while number<10:\n",
    "    number+=1\n",
    "    \n",
    "    if number%2==0:\n",
    "        continue\n",
    "    else:\n",
    "        print(number)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "c04be9a2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Please enter your age: 34\n",
      "Ticket price is $15\n"
     ]
    },
    {
     "ename": "KeyboardInterrupt",
     "evalue": "Interrupted by user",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-8-7bdf77d902cd>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[0mprompt\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m\"\\nPlease enter your age: \"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;32mwhile\u001b[0m \u001b[1;32mTrue\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 4\u001b[1;33m     \u001b[0mage\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0minput\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mprompt\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      5\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0mage\u001b[0m\u001b[1;33m<\u001b[0m\u001b[1;36m3\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\ipykernel\\kernelbase.py\u001b[0m in \u001b[0;36mraw_input\u001b[1;34m(self, prompt)\u001b[0m\n\u001b[0;32m    858\u001b[0m                 \u001b[1;34m\"raw_input was called, but this frontend does not support input requests.\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    859\u001b[0m             )\n\u001b[1;32m--> 860\u001b[1;33m         return self._input_request(str(prompt),\n\u001b[0m\u001b[0;32m    861\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_parent_ident\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    862\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_parent_header\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\ipykernel\\kernelbase.py\u001b[0m in \u001b[0;36m_input_request\u001b[1;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[0;32m    902\u001b[0m             \u001b[1;32mexcept\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    903\u001b[0m                 \u001b[1;31m# re-raise KeyboardInterrupt, to truncate traceback\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 904\u001b[1;33m                 \u001b[1;32mraise\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Interrupted by user\"\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    905\u001b[0m             \u001b[1;32mexcept\u001b[0m \u001b[0mException\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    906\u001b[0m                 \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mlog\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mwarning\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Invalid Message:\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mexc_info\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m: Interrupted by user"
     ]
    }
   ],
   "source": [
    "age=5\n",
    "prompt=\"\\nPlease enter your age: \"\n",
    "while True:\n",
    "    age=int(input(prompt))\n",
    "    \n",
    "    if age<3:\n",
    "        print(\"Ticket is Free\")\n",
    "    elif age<12 and age>3:\n",
    "        print(\"Ticket price is $10\")\n",
    "    elif age>12:\n",
    "        print(\"Ticket price is $15\")\n",
    "        \n",
    "        break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "22b0284f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Verifying ghj\n",
      "Verifying sdf\n",
      "Verifying asd\n",
      "['ghj', 'sdf', 'asd']\n"
     ]
    }
   ],
   "source": [
    "unconfirmedusers=['asd','sdf','ghj']\n",
    "confirmedusers=[]\n",
    "\n",
    "while unconfirmedusers:\n",
    "    currentuser=unconfirmedusers.pop()\n",
    "    print(f\"Verifying {currentuser}\")\n",
    "    \n",
    "    confirmedusers.append(currentuser)\n",
    "    \n",
    "\n",
    "print(confirmedusers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "b27cd71d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['dog', 'mouse', 'rat', 'dog']\n"
     ]
    }
   ],
   "source": [
    "pets = ['cat','dog','mouse','rat','cat','dog']\n",
    "\n",
    "while 'cat' in pets:\n",
    "    \n",
    "    pets.remove('cat')\n",
    "\n",
    "print(pets)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "fc4a21cf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your name: wwqww\n",
      "Which mountain who would like to climb?:asdad\n",
      "Would you like to add another user? (Yes/No):Yes\n",
      "Enter your name: ddedew\n",
      "Which mountain who would like to climb?:dwdwdw\n",
      "Would you like to add another user? (Yes/No):Yes\n",
      "Enter your name: add\n",
      "Which mountain who would like to climb?:adwd\n",
      "Would you like to add another user? (Yes/No):No\n",
      "wwqww wants to climb Mountain asdad\n",
      "ddedew wants to climb Mountain dwdwdw\n",
      "add wants to climb Mountain adwd\n"
     ]
    }
   ],
   "source": [
    "polling=True\n",
    "\n",
    "responses={}\n",
    "\n",
    "while polling:\n",
    "    \n",
    "    name=input(\"Enter your name: \")\n",
    "    response=input(\"Which mountain who would like to climb?:\")\n",
    "    \n",
    "    responses[name]=response\n",
    "    \n",
    "    check= input(\"Would you like to add another user? (Yes/No):\")\n",
    "    \n",
    "    if check==\"No\":\n",
    "        polling=False\n",
    "        \n",
    "for name,response in responses.items():\n",
    "    print( f\"{name} wants to climb Mountain {response}\")\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "02406f21",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Nishith Shetty\n"
     ]
    }
   ],
   "source": [
    "def fullname(x,y):\n",
    "     \n",
    "        fullname=f\"{x} {y}\"\n",
    "        return fullname\n",
    "    \n",
    "name=fullname('Nishith','Shetty')\n",
    "print(name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "741404af",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Nishith Shetty\n"
     ]
    }
   ],
   "source": [
    "def fullname(x,y):\n",
    "     \n",
    "    print(f\"{x} {y}\")\n",
    "       \n",
    "    \n",
    "fullname('Nishith','Shetty')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "aed9bb2b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I have a Dog\n",
      "My Dog name is Punda\n"
     ]
    }
   ],
   "source": [
    "def animal(animal,animal_name):\n",
    "    \n",
    "    print(f\"I have a {animal}\")\n",
    "    print(f\"My {animal} name is {animal_name}\")\n",
    "    \n",
    "    \n",
    "c=animal(animal='Dog',animal_name='Punda')          "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "69eb473b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Nisith N Shetty\n",
      "Nisith Shetty\n"
     ]
    }
   ],
   "source": [
    "def name(f,l,m=\"\"):\n",
    "    if m:\n",
    "        print(f\"{f} {m} {l}\")\n",
    "    else:\n",
    "        print(f\"{f} {l}\")\n",
    "        \n",
    "name('Nisith','Shetty','N')\n",
    "name('Nisith','Shetty')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "657a4a35",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Nisith Shetty\n"
     ]
    },
    {
     "ename": "TypeError",
     "evalue": "'str' object is not callable",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-2-cb0ae288d1dc>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     10\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mname\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     11\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 12\u001b[1;33m \u001b[0mname\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mname\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'Nisith'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m'Shetty'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m'N'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     13\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mname\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: 'str' object is not callable"
     ]
    }
   ],
   "source": [
    "def name(f,l,m=''):\n",
    "    if m:\n",
    "        fn= f\"{f} {m} {l}\"\n",
    "    else:\n",
    "        fn=f\"{f} {l}\"\n",
    "     \n",
    "    return fn\n",
    "\n",
    "name=name('Nisith','Shetty')\n",
    "print(name)\n",
    "\n",
    "name=name('Nisith','Shetty','N')\n",
    "print(name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "16d998b5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Nisith Shetty\n"
     ]
    }
   ],
   "source": [
    "def name(f,l,m=''):\n",
    "    if m:\n",
    "        fn= f\"{f} {m} {l}\"\n",
    "    else:\n",
    "        fn=f\"{f} {l}\"\n",
    "     \n",
    "    return fn\n",
    "\n",
    "name=name('Nisith','Shetty')\n",
    "print(name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "b8c62fac",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'First': 'Nisith', 'Last': 'Shetty'}\n"
     ]
    }
   ],
   "source": [
    "def fullname(Firstname,Lastname):\n",
    "    fullnames={'First':Firstname,'Last':Lastname}\n",
    "    return fullnames\n",
    "\n",
    "name=fullname('Nisith','Shetty')\n",
    "\n",
    "print(name)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "573e77a1",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "'continue' not properly in loop (<ipython-input-17-d63f03492ff8>, line 6)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  File \u001b[1;32m\"<ipython-input-17-d63f03492ff8>\"\u001b[1;36m, line \u001b[1;32m6\u001b[0m\n\u001b[1;33m    continue\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m 'continue' not properly in loop\n"
     ]
    }
   ],
   "source": [
    "def fullname(Firstname,Lastname,age=''):\n",
    "    fullnames={'First':Firstname,'Last':Lastname}\n",
    "    if age:\n",
    "        fullnames['age']=age\n",
    "        \n",
    "    return fullnames\n",
    "\n",
    "name= fullname('Nisith','Shetty','25')\n",
    "\n",
    "print(name)\n",
    "    \n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "5b36720b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter first name:nishith\n",
      "Enter Last name:shetty\n",
      "Nishith Shetty\n"
     ]
    },
    {
     "ename": "KeyboardInterrupt",
     "evalue": "Interrupted by user",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-26-da39565162ce>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;32mwhile\u001b[0m \u001b[1;32mTrue\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 6\u001b[1;33m     \u001b[0mFirstname\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0minput\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34mf\"Enter first name:\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      7\u001b[0m     \u001b[1;32mif\u001b[0m \u001b[0mFirstname\u001b[0m\u001b[1;33m==\u001b[0m\u001b[1;34m'q'\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      8\u001b[0m         \u001b[1;32mbreak\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\ipykernel\\kernelbase.py\u001b[0m in \u001b[0;36mraw_input\u001b[1;34m(self, prompt)\u001b[0m\n\u001b[0;32m    858\u001b[0m                 \u001b[1;34m\"raw_input was called, but this frontend does not support input requests.\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    859\u001b[0m             )\n\u001b[1;32m--> 860\u001b[1;33m         return self._input_request(str(prompt),\n\u001b[0m\u001b[0;32m    861\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_parent_ident\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    862\u001b[0m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0m_parent_header\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\ipykernel\\kernelbase.py\u001b[0m in \u001b[0;36m_input_request\u001b[1;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[0;32m    902\u001b[0m             \u001b[1;32mexcept\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    903\u001b[0m                 \u001b[1;31m# re-raise KeyboardInterrupt, to truncate traceback\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 904\u001b[1;33m                 \u001b[1;32mraise\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Interrupted by user\"\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[1;32mNone\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    905\u001b[0m             \u001b[1;32mexcept\u001b[0m \u001b[0mException\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    906\u001b[0m                 \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mlog\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mwarning\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Invalid Message:\"\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mexc_info\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mTrue\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m: Interrupted by user"
     ]
    }
   ],
   "source": [
    "def fullname(Firstname,Lastname):\n",
    "    fullnames=f\"{Firstname} {Lastname}\"\n",
    "    return fullnames\n",
    "\n",
    "while True:\n",
    "    Firstname=input(f\"Enter first name:\")\n",
    "    if Firstname=='q':\n",
    "        break\n",
    "        \n",
    "    Lastname=input(f\"Enter Last name:\")\n",
    "    if Lastname=='q':\n",
    "        break\n",
    "    \n",
    "    if Firstname=='q'or Lastname=='q':\n",
    "        break\n",
    "    else:\n",
    "\n",
    "        formatted_names= fullname(Firstname,Lastname)\n",
    "        print(formatted_names.title())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "d7dea87a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bangalore, India\n"
     ]
    }
   ],
   "source": [
    "def city_country(city,country):\n",
    "    name=f'{city}, {country}'\n",
    "    return name\n",
    "\n",
    "\n",
    "m=city_country('Bangalore','India')\n",
    "print(m)\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "de569073",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello, Nishith!\n",
      "Hello, Akshay!\n",
      "Hello, Rohit!\n",
      "['Nishith', 'Akshay', 'Rohit']\n"
     ]
    }
   ],
   "source": [
    "#Greet Users\n",
    "\n",
    "def greet(persons):\n",
    "    printed=[]\n",
    "    for name in persons:\n",
    "        printed.append(name)\n",
    "        print(f\"Hello, {name}!\")\n",
    "    print(printed)    \n",
    "\n",
    "\n",
    "    \n",
    "persons=['Nishith','Akshay','Rohit']\n",
    "greet(persons)\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "d508f12f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "dodechedron is completed\n",
      "robot is completed\n",
      "phone is completed\n",
      "\n",
      "Completed items list: \n",
      "dodechedron\n",
      "robot\n",
      "phone\n"
     ]
    }
   ],
   "source": [
    "unprinted = ['phone','robot','dodechedron']\n",
    "completed=[]\n",
    "\n",
    "while unprinted:\n",
    "    complete = unprinted.pop()\n",
    "    completed.append(complete)\n",
    "    print(f\"{complete} is completed\")\n",
    "    \n",
    "print(\"\\nCompleted items list: \")\n",
    "for name in completed:\n",
    "    print(name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "a8adbbd7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "phone is completed\n",
      "robot is completed\n",
      "dodechedron is completed\n",
      "\n",
      "Completed items list: \n",
      "phone\n",
      "robot\n",
      "dodechedron\n"
     ]
    }
   ],
   "source": [
    "unprinted = ['phone','robot','dodechedron']\n",
    "completed=[]\n",
    "\n",
    "for un in unprinted:\n",
    "    completed.append(un)\n",
    "    print(f\"{un} is completed\")\n",
    "    \n",
    "print(\"\\nCompleted items list: \")\n",
    "for name in completed:\n",
    "    print(name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "1e82f397",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Printing Model:dodechedron\n",
      "Printing Model:robot\n",
      "Printing Model:phone\n",
      "\n",
      "The following models have been printed:\n",
      "dodechedron\n",
      "robot\n",
      "phone\n"
     ]
    }
   ],
   "source": [
    "def unprited_func(unprinted, printed):\n",
    "    while unprinted:\n",
    "        complete=unprinted.pop()\n",
    "        printed.append(complete)\n",
    "        print(f\"Printing Model:{complete}\")\n",
    "\n",
    "def list_printed(printed):\n",
    "    print(f\"\\nThe following models have been printed:\")\n",
    "    for name in printed:\n",
    "        print(name)\n",
    "        \n",
    "unprinted1 = ['phone','robot','dodechedron']\n",
    "completed1=[]\n",
    "\n",
    "unprited_func(unprinted1, completed1)\n",
    "list_printed(completed1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "2c6cae50",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Printing Model:dodechedron\n",
      "Printing Model:robot\n",
      "Printing Model:phone\n",
      "\n",
      "The following models have been printed:\n",
      "dodechedron\n",
      "robot\n",
      "phone\n",
      "[]\n"
     ]
    }
   ],
   "source": [
    "def unprited_func(unprinted, printed):\n",
    "    while unprinted:\n",
    "        complete=unprinted.pop()\n",
    "        printed.append(complete)\n",
    "        print(f\"Printing Model:{complete}\")\n",
    "\n",
    "def list_printed(printed):\n",
    "    print(f\"\\nThe following models have been printed:\")\n",
    "    for name in printed:\n",
    "        print(name)\n",
    "        \n",
    "unprinted1 = ['phone','robot','dodechedron']\n",
    "completed1=[]\n",
    "\n",
    "#Make a copy of the list\n",
    "unprited_func(unprinted1[:], completed1)\n",
    "list_printed(completed1)\n",
    "print(unprinted1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "d9c371cd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hi\n",
      "Hello\n",
      "Who\n",
      "Nakkan\n"
     ]
    }
   ],
   "source": [
    "\n",
    "\n",
    "def show_messages(message):\n",
    "    for name in message:\n",
    "        print(name)\n",
    "        \n",
    "words=['Hi','Hello','Who','Nakkan']\n",
    "show_messages(words)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "6d258c61",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hi\n",
      "Hello\n",
      "Who\n",
      "Nakkan\n",
      "['Hi', 'Hello', 'Who', 'Nakkan']\n"
     ]
    }
   ],
   "source": [
    "def show_messages(message,sentmessage):\n",
    "    for name in message:\n",
    "        sentmessage.append(name)\n",
    "        print(name)\n",
    "    print(sentmessage)\n",
    "\n",
    "words=['Hi','Hello','Who','Nakkan']\n",
    "sentmessage=[]\n",
    "\n",
    "show_messages(words,sentmessage)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "5e6fed8e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Nakkan\n",
      "Who\n",
      "Hello\n",
      "Hi\n",
      "['Nakkan', 'Who', 'Hello', 'Hi']\n"
     ]
    }
   ],
   "source": [
    "def show_messages(message,sentmessage):\n",
    "    while message:\n",
    "        newlist=message.pop()\n",
    "        sentmessage.append(newlist)\n",
    "        print(newlist)\n",
    "    print(sentmessage)\n",
    "\n",
    "words=['Hi','Hello','Who','Nakkan']\n",
    "sentmessage=[]\n",
    "\n",
    "show_messages(words,sentmessage)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "59703c60",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Nakkan\n",
      "Who\n",
      "Hello\n",
      "Hi\n",
      "['Nakkan', 'Who', 'Hello', 'Hi']\n",
      "[]\n"
     ]
    }
   ],
   "source": [
    "def show_messages(message,sentmessage):\n",
    "    while message:\n",
    "        newlist=message.pop()\n",
    "        sentmessage.append(newlist)\n",
    "        print(newlist)\n",
    "    print(sentmessage)\n",
    "\n",
    "words=['Hi','Hello','Who','Nakkan']\n",
    "sentmessage=[]\n",
    "\n",
    "show_messages(words,sentmessage)\n",
    "print(words)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "bf01ff93",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "as\n",
      "adf\n",
      "wer\n",
      "qwe\n",
      "bnm\n"
     ]
    }
   ],
   "source": [
    "def sandwiches(*args):\n",
    "    for n in args:\n",
    "        print(n)\n",
    "        \n",
    "\n",
    "sandwiches('as','adf','wer','qwe','bnm')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "570009ba",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'Country': 'India', 'firstname': 'Nishith', 'lastname': 'Shetty'}\n"
     ]
    }
   ],
   "source": [
    "def build_profile(firstname,lastname,**profile):\n",
    "    profile['firstname']=firstname.title()\n",
    "    profile['lastname']=lastname.title()\n",
    "    return profile\n",
    "    \n",
    "\n",
    "user_profile=build_profile('nishith','shetty',Country='India')\n",
    "print(user_profile)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "df9143a3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'firstname': 'Nishith', 'lastname': 'Shetty'}\n"
     ]
    }
   ],
   "source": [
    "def build_profile(firstname,lastname):\n",
    "    profile['firstname']=firstname.title()\n",
    "    profile['lastname']=lastname.title()\n",
    "    return profile\n",
    "    \n",
    "\n",
    "user_profile=build_profile('nishith','shetty')\n",
    "print(user_profile)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "e25d80e5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'firstname': 'Nishith', 'lastname': 'Shetty'}\n"
     ]
    }
   ],
   "source": [
    "def build_profile(firstname,lastname):\n",
    "    profile['firstname']=firstname.title()\n",
    "    profile['lastname']=lastname.title()\n",
    "    print(profile)\n",
    "    \n",
    "\n",
    "build_profile('nishith','shetty')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "bd76ff5b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'color': 'blue', 'tom_package': True, 'Manufacturer': 'subaru', 'Model Name': 'outback'}\n"
     ]
    }
   ],
   "source": [
    "def car_details(manufac,modelname,**details):\n",
    "    details['Manufacturer']=manufac\n",
    "    details['Model Name']=modelname\n",
    "    return details\n",
    "\n",
    "cardet=car_details('subaru','outback',color='blue',tom_package=True)\n",
    "print(cardet)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f365026a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
