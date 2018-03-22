IGitt.Utils.__init__.py CachedDataMixin #Collects all the data and writes it into self.data

#Common Errors
401: Unauthorized #Are you sure you are using the right token (Oauth/Private)

#Interface
Dictates the attributes being used in igitt
--> When writing a new implementation, you need a getter and a setter for every attribute mentioned in the Interface
##Example
Inteface | Implementation | GitLab API V4
number | number | id # done
x | x | iid # done
x | x | project_id # done
scope | scope | x # TODO wie muss das rein?
title | title | title
description | description | description
state | state | state
created | created | created_at
updated | updated | updated_at
group | x | x
issues | x | x
merge_requests | x | x
