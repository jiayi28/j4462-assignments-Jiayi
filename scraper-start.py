import urllib2, csv
import mechanize
from bs4 import BeautifulSoup

br = mechanize.Browser()
br.open('http://enrarchives.sos.mo.gov/enrnet/PickaRace.aspx')

# Fill out the top form
br.select_form(nr=0)
br.form['ctl00$MainContent$cboElectionNames'] = ['750003566']
br.submit('ctl00$MainContent$btnElectionType')

# Fill out the bottom form
br.select_form(nr=0)
br.form['ctl00$MainContent$cboRaces'] = ['750003269']
br.submit('ctl00$MainContent$btnCountyChange')

# Get HTML
html = br.response().read()

########## YOUR CODE HERE ##########

outfile = open('mo_primary_election.csv', 'w')
writer = csv.writer(outfile)

soup = BeautifulSoup(html, "html.parser")

table = soup.find('table', {'class':'electtable'})

rows = table.find_all('tr')

for row in rows:
	data = [cell.text.encode('utf-8') for cell in row.find_all('td')[0:]]
	writer.writerow(data)


