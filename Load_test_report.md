Type	Name	# Requests	# Fails	Average (ms)	Min (ms)	Max (ms)	Average size (bytes)	RPS	Failures/s
POST	/predict	6153	6153	6.45	2	45	22	4.69	4.69
Aggregated	6153	6153	6.45	2	45	22	4.69	4.69
Response Time Statistics
Method	Name	50%ile (ms)	60%ile (ms)	70%ile (ms)	80%ile (ms)	90%ile (ms)	95%ile (ms)	99%ile (ms)	100%ile (ms)
POST	/predict	7	7	8	8	9	10	11	45
Aggregated	7	7	8	8	9	10	11	45
Failures Statistics
# Failures	Method	Name	Message
6153	POST	/predict	HTTPError('404 Client Error: Not Found for url: /predict')
