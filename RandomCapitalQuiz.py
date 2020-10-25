# RandomCapitalQuiz.py

import random
capitals = {'Afghanistan':'Kabul', 'Albania':'Tirana', 'Algeria':'Algiers', 'American Samoa (USA)':'Pago Pago', 'Andorra':'Andorra La Vella', 'Angola':'Luanda', 'Anguilla (UK)':'The Valley', 'Antigua and Barbuda':'Saint Johns', 'Argentina':'Buenos Aires', 'Armenia':'Yerevan', 'Aruba (Netherlands)':'Oranjestad', 'Australia':'Canberra', 'Austria':'Vienna', 'Azerbaijan':'Baku', 'Bahamas':'Nassau', 'Bahrain':'Manama', 'Bangladesh':'Dhaka', 'Barbados':'Bridgetown', 'Belarus':'Minsk', 'Belgium':'Brussels', 'Belize':'Belmopan', 'Benin':'Porto-Novo', 'Bermuda (UK)':'Hamilton', 'Bhutan':'Thimphu', 'Bolivia':'Sucre', 'Bosnia and Herzegovina':'Sarajevo', 'Botswana':'Gaborone', 'Brazil':'Brasília', 'British Virgin Islands (UK)':'Road Town', 'Brunei':'Bandar Seri Begawan', 'Bulgaria':'Sofia', 'Burkina Faso':'Ouagadougou', 'Burundi':'Bujumbura', 'Cambodia':'Phnom Penh', 'Cameroon':'Yaoundé', 'Canada':'Ottawa', 'Cape Verde':'Praia', 'Cayman Islands (UK)':'George Town', 'Central African Republic':'Bangui', 'Chad':'NDjamena', 'Chile':'Santiago', 'China':'Beijing', 'Christmas Island (Australia)':'Flying Fish Cove', 'Cocos (Keeling) Islands (Australia)':'West Island, Cocos Islands', 'Colombia':'Bogotá', 'Comoros':'Moroni', 'Cook Islands (New Zealand)':'Avarua', 'Costa Rica':'San José', 'Croatia':'Zagreb', 'Cuba':'Havana', 'Curacao (Netherlands)':'Willemstad', 'Cyprus':'Nicosia', 'Czech Republic':'Prague', 'D.R Congo':'Kinshasa', 'Denmark':'Copenhagen', 'Djibouti':'Djibouti-city', 'Dominica':'Roseau', 'Dominican Republic':'Santo Domingo', 'East Timor (Timor-Leste)':'Dili', 'Ecuador':'Quito', 'Egypt':'Cairo', 'El Salvador':'San Salvador', 'Equatorial Guinea':'Malabo', 'Eritrea':'Asmara', 'Estonia':'Tallinn', 'Ethiopia':'Addis Ababa', 'Falkland Islands (UK)':'Stanley', 'Faroe Islands (Denmark)':'Tórshavn', 'Fiji':'Suva', 'Finland':'Helsinki', 'France':'Paris', 'French Guiana (France)':'Cayenne', 'French Polynesia (France)':'Papeete', 'Gabon':'Libreville', 'Gambia':'Banjul', 'Georgia':'Tbilisi', 'Germany':'Berlin', 'Ghana':'Accra', 'Gibraltar (UK)':'Gibraltar', 'Greece':'Athens', 'Greenland (Denmark)':'Nuuk', 'Grenada':'St. Georges', 'Guam (USA)':'Hagatna', 'Guatemala':'Guatemala City', 'Guernsey (UK)':'Saint Peter Port', 'Guinea':'Conakry', 'Guinea-Bissau':'Bissau', 'Guyana':'Georgetown', 'Haiti':'Port-au-prince', 'Honduras':'Tegucigalpa', 'Hong Kong (China)':'Hong Kong City', 'Hungary':'Budapest', 'Iceland':'Reykjavík', 'India':'New Delhi', 'Indonesia':'Jakarta', 'Iran':'Tehran', 'Iraq':'Baghdad', 'Ireland':'Dublin', 'Isle of Man (UK)':'Douglas', 'Israel':'Jerusalem', 'Italy':'Rome', 'Ivory Coast':'Yamoussoukro', 'Jamaica':'Kingston', 'Japan':'Tokyo', 'Jersey (UK)':'Saint Helier', 'Jordan':'Amman', 'Kazakhstan':'Astana', 'Kenya':'Nairobi', 'Kiribati':'Tarawa', 'Kosovo':'Pristina', 'Kuwait':'Kuwait City', 'Kyrgyzstan':'Bishkek', 'Laos':'Vientiane', 'Latvia':'Riga', 'Lebanon':'Beirut', 'Lesotho':'Maseru', 'Liberia':'Monrovia', 'Libya':'Tripoli', 'Liechtenstein':'Vaduz', 'Lithuania':'Vilnius', 'Luxembourg':'Luxembourg', 'Macedonia':'Skopje', 'Madagascar':'Antananarivo', 'Malawi':'Lilongwe', 'Malaysia':'Kuala Lumpur', 'Maldives':'Malé', 'Mali':'Bamako', 'Malta':'Valletta', 'Marshall Islands':'Majuro', 'Mauritania':'Nouakchott', 'Mauritius':'Port Louis', 'Mexico':'Mexico City', 'Micronesia':'Palikir', 'Moldova':'Chisinau', 'Monaco':'Monaco', 'Mongolia':'Ulan Bator', 'Montenegro':'Podgorica', 'Montserrat (UK)':'Brades, Plymouth', 'Morocco':'Rabat', 'Mozambique':'Maputo', 'Myanmar':'Naypyidaw', 'Namibia':'Windhoek', 'Nauru':'Yaren', 'Nepal':'Kathmandu', 'Netherlands':'Amsterdam', 'New Caledonia (France)':'Nouméa', 'New Zealand':'Wellington', 'Nicaragua':'Managua', 'Niger':'Niamey', 'Nigeria':'Abuja', 'Niue (New Zealand)':'Alofi', 'Norfolk Island (Australia)':'Kingston', 'North Korea':'Pyongyang', 'Northern Mariana Islands (USA)':'Saipan', 'Norway':'Oslo', 'Oman':'Muscat', 'Pakistan':'Islamabad', 'Palau':'Ngerulmud', 'Palestine':'Ramallah and Gaza', 'Panama':'Panama City', 'Papua New Guinea':'Port Moresby', 'Paraguay':'Asunción', 'Peru':'Lima', 'Philippines':'Manila', 'Pitcairn Islands (UK)':'Adamstown', 'Poland':'Warsaw', 'Portugal':'Lisbon', 'Puerto Rico (USA)':'San Juan', 'Qatar':'Doha', 'Republic of the Congo':'Brazzaville', 'Romania':'Bucharest', 'Russia':'Moscow', 'Rwanda':'Kigali', 'Saint Barthelemy':'Gustavia, Saint Barthélemy', 'Saint Helena, Ascension, and Tristan da Cunha (UK)':'Jamestown', 'Saint Kitts and Nevis':'Basseterre', 'Saint Lucia':'Castries', 'Saint Martin':'Marigot', 'Saint Pierre and Miquelon (France)':'Saint-Pierre', 'Saint Vincent and the Grenadines':'Kingstown', 'Samoa':'Apia', 'San Marino':'San Marino', 'São Tomé and Príncipe':'Sao Tome', 'Saudi Arabia':'Riyadh', 'Senegal':'Dakar', 'Serbia':'Belgrade', 'Seychelles':'Victoria', 'Sierra Leone':'Freetown', 'Singapore':'Singapore', 'Sint Maarten (Netherlands)':'Philipsburg', 'Slovakia':'Bratislava', 'Slovenia':'Ljubljana', 'Solomon Islands':'Honiara', 'Somalia':'Mogadishu', 'South Africa':'Cape Town', 'South Korea':'Seoul', 'South Sudan':'Juba', 'Spain':'Madrid', 'Sri Lanka':'Sri Jayawardenapura-kotte', 'Sudan':'Khartoum', 'Suriname':'Paramaribo', 'Eswatini(Swaziland)':'Mbabane', 'Sweden':'Stockholm', 'Switzerland':'Bern', 'Syria':'Damascus', 'Taiwan':'Taipei', 'Tajikistan':'Dushanbe', 'Tanzania':'Dodoma', 'Thailand':'Bangkok', 'Togo':'Lomé', 'Tokelau (New Zealand)':'Nukunonu, Atafu,Tokelau', 'Tonga':'Nukualofa', 'Transnistria':'Tiraspol', 'Trinidad and Tobago':'Port of Spain', 'Tunisia':'Tunis', 'Turkey':'Ankara', 'Turkmenistan':'Ashgabat', 'Turks and Caicos Islands (UK)':'Cockburn Town', 'Tuvalu':'Funafuti', 'Uganda':'Kampala', 'Ukraine':'Kiev', 'United Arab Emirates':'Abu Dhabi', 'United Kingdom':'London', 'United States':'Washington D.C.', 'United States Virgin Islands (USA)':'Charlotte Amalie', 'Uruguay':'Montevideo', 'Uzbekistan':'Tashkent', 'Vanuatu':'Port Vila', 'Vatican City':'Vatican City', 'Venezuela':'Caracas', 'Vietnam':'Hanoi', 'Wallis and Futuna (France)':'Mata-Utu', 'Western Sahara':'El Aaiun', 'Yemen':'Sanaa', 'Zambia':'Lusaka', 'Zimbabwe':'Harare'}
play = 'Y'
quizNum = 0
gotCorrect = 0

while (play == 'Y' or play == 'y'):
	print('\n', ('*' * 80),'\n')
	print((' ' * 20) + 'Country Capitals Quiz (Question %s)' % (quizNum + 1))
	print('\n')

	countries = list(capitals.keys())
	random.shuffle(countries)

	questionNum = random.randint(1, 236)

	correctAnswer = capitals[countries[questionNum]]
	wrongAnswers = list(capitals.values())
	del wrongAnswers[wrongAnswers.index(correctAnswer)]
	wrongAnswers = random.sample(wrongAnswers, 3)
	answerOptions = wrongAnswers + [correctAnswer]
	random.shuffle(answerOptions)

	print('Q. What is the capital of %s?\n' % (countries[questionNum]))
	for i in range(4):
			print(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
	print('\n')

	getAnswer = input("Enter answer: (Q to quit) ").title()

	if getAnswer.upper() == 'ABCD'[answerOptions.index(correctAnswer)]:
		print("Correct!!!")
		gotCorrect += 1
	elif getAnswer.upper() == 'Q':
		play = 'N'
		break
	else:
		print("Incorrect")

	print("The answer is ", 'ABCD'[answerOptions.index(correctAnswer)],":", correctAnswer, '\n')
	quizNum += 1

print('\n', ('*' * 80),'\n\n')
print("You answered %s questions and you scored: %s points" % (quizNum, gotCorrect))
