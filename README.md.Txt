README for News Log Analysis for Full Stack Web Developer Nanodegree

Latest Version: 5/17/2017

The purpose of this program is to run queries on a database of requests to a news website--particular goals of this program are to identify the
3 most popular news articles (including the number of views for each), the total number of views each of the contributing authors have had on his/her stories,
and finally, to identify the days (if any) that more than 1% of the visits to the website resulted in errors.

Files included with this program:
newsdata.sql--contains the database setup that will support the backend of the item catalog using PostgreSQL
news_queries.py--contains the python code necessary to retrieve the answers to the above queries.

The database setup contains 3 base tables. The articles table contains all of the information about the articles available on the site including author (by author id),
title, slug, lead, body, time, and id.  The authors table contains author information including name, bio, and id.  Finally the log table contains all of the access
data for the website including the path of the url accessed, ip address requesting, method, status, time, and id of the request.

Further, this project makes use of 3 views, which were generated with the following statements:

Number of times the 3 most popular articles were accessed:

create view pathnum as SELECT path, count(*) as num from log group by path order by num desc limit 4 offset 1;

Number of views for a given author:

create view authnum as SELECT articles.author, count(*) as num FROM articles, log WHERE log.path like '%' || articles.slug 
	 		GROUP BY articles.author ORDER BY num desc;

To get the number of 404 responses and total request organized by day:

create view req_and_errs as SELECT date(time) as day, count(case when status = '404 NOT FOUND' then 1 else null end) as errors,
				count(status) as total_req FROM log GROUP BY day;

To run this program you will need to download Virtual Box and Vagrant to support the databases
needed to use this program.  Using git you can clone all of the necessary files for this program from Udacity via 
http://github.com/udacity/fullstack-nanodegree-vm fullstack

Once the above softwares are downloaded, start the virtual machine by typing vagrant up and log in to the virtual machine by typing vagrant ssh.
Type cd /vagrant and cd to 'News_Log to access the project folder.
Run the python program named news_queries.py to connect to the database and retrieve the information outlined in the beginning of this document.

You can disconnect from the VM by typing ctrl + D and typing logout.

Sample Output of the Program:

Candidate is jerk, alleges rival - 338647 views
Bears love berries, alleges bear - 253801 views
Bad things gone, say good people - 170098 views
Ursula La Multa - 507594 views
Rudolf von Treppenwitz - 423457 views
Anonymous Contributor - 170098 views
Markoff Chaney - 84557 views
2016-07-17 - 2.26% errors



