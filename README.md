# interview-python


## Step 1

Given a list of URLs as the input (one per line), return the status code that they return. The URLs should be checked sequentially.

Example input:

	https://www.google.com/
	https://www.google.com/thisdoesnotexist

Example invocation:

	python app.py < urls.txt

Example output:

	[302] https://www.google.com/
	[404] https://www.google.com/thisdoesnotexist


## Step 2

Create a `Dockerfile` for it.

Example invocation:

	docker run -it app < urls.txt
	

## Step 3

Create some unit tests mocking the HTTP call so there's no traffic coming out

Example invocation:

	docker run -it app test.sh

	
## Step 4

Make it concurrent by using threads.

Example invocation:

	docker run -it app -k threading
	
	
## Step 5

Make it parallel by using processes.

Example invocation:

	docker run -it app -k multiprocessing

