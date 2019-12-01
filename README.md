### Json Schema Validator & Path Query with Python Falcon

-------------

** Json Schema Validator and JSON Path For Python Api Developers **

#### Quick Run 

```sh
git clone https://github.com/makseli/falcon-json-schema-validate-path-query.git
cd falcon-json-schema-validate-path-query
docker-compose up 
```
Open your browser with -> http://127.0.0.1:3499

-------------

#### Run 
- Firstly, run ```sh docker-compose up -p json-schema-query-falcon-python```
- Open your browser with http://127.0.0.1:3499
- [ POST ] /path-query with raw application/json -> 
```json 
{
    "set_json_path": "$.aggregations.sample.keywords.bucket[*][?(@.doc_count>109)]",
    "set_json_data": {
        "aggregations": {
            "sample": {
                "doc_count": 200,
                "keywords": {
                    "doc_count": 200,
                    "bg_count": 650,
                    "bucket": [
                        {
                            "key": "elasticsearch",
                            "doc_count": 110,
                            "score": 1.078125,
                            "bg_count": 200
                        },
                        {
                            "key": "elk",
                            "doc_count": 150,
                            "score": 1.078125,
                            "bg_count": 200
                        },
                        {
                            "key": "logstash",
                            "doc_count": 50,
                            "score": 0.5625,
                            "bg_count": 50
                        },
                        {
                            "key": "kibana",
                            "doc_count": 50,
                            "score": 0.5625,
                            "bg_count": 50
                        }
                    ]
                }
            }
        }
    }
}

```

- [ POST ] /validate-json with raw application/json -> 
```json 
{
	"set_data" : {
		"book_name" : "The Greatest Turkish People"
	},
	"set_schema" : {
        "type": "object",
          "required": [
            "book_name"
            ],
        "properties": {
            "book_name": { "type": "string" }
        }
    }
}
