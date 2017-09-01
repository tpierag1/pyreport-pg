# PyReport-PG

PyReport-PG is a script that allows a user to run a variety
of reports on the Udacity Fullstack Nano Degree Vagrant VM.

The VM contains a running version of Postgresql with a number of databases.
For the purposes of this exercise the relevant database is called 'news'

Within this database are three tables; articles, authors, and log.

The articles table contains the following columns:
- author
- title
- slug
- lead
- body
- time
- id

The authors table contains the following columns:
- name
- bio
- id

The log table contains the following columns:
- path
- ip
- method
- status
- time
- id

Pyreport is capable of running the following reports:

- Report detailing the three most widely read articles

- Report detailing the most widely read authors

- Report detailing days in which errors for pages reached over 1%

### Requirements
To run the script requires the following dependencies:
- Virtualbox
- Vagrant

### Setup

Before running the script the following steps need to be taken:

First clone the Vagrant machine, go to fullstack-nanodegree-vm directory
and clone directory

`git clone https://github.com/udacity/fullstack-nanodegree-vm.git fullstack`

`cd fullstack/vagrant`

`git clone https://github.com/tpierag1/pyreport-pg.git`

Also, download and unzip the database schema and data for the database

`wget https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip`
`unzip newsdata.zip`

Next, start vagrant machine and SSH in

`vagrant up`

After machine starts

`vagrant ssh`

Then go to /vagrant directory

`cd /vagrant`

From there import the schema and data into the database

`psql -d news -f newsdata.sql`

Next, access the database using the psql command

`psql -d news`

Finally, set up the necessary views within the database

```sql

create view author_views as select articles.author, count (path) as views from
log, articles where articles.slug = substring(log.path, 10) group
by articles.author;
```

```sql

create view total as select time::date, count(*) as num from log group by
time::date order by num;
```

```sql

create view error as select time::date, count(*) as num from log where
status not like '%200%' group by time::date order by num;
```

```sql

create view calc as select total.time, cast(error.num*100 as float)/
cast(total.num as float) as val from error, total where error.time=total.time;
```

### Using script

To use the script run pyreport.py from the /vagrant directory within the
vagrant machine

`cd /vagrant`

`python3 pyreport.py`

This will present the user with a series of options for running reports

Please Select Option:

1: Run Top Articles Report

2: Run Top Authors Report

3: Run Errors Greater That 1% Per Day Report

4: Run All Reports


Choose the option for the report that you want to run.
