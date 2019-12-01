# -*- coding:utf-8 -*-

book_data = '''{
          "book_id": 1001,
          "book_name": "Çocuklar için Maker Kitaplığı Seti",
          "book_link": "https://www.robotistan.com/cocuklar-icin-maker-kitapligi-seti",
          "book_price": 202.34,
          "book_description" : "Programcı (coder) olmak zorundasın, Hacker olmak zorundasın..."
        }'''

book_schema = '''{
        "type": "object",
          "required": [
            "book_id",
            "book_name"
            ],
        "properties": {
            "book_id": { "type": "number" },
            "book_name": { "type": "string" },
            "book_link": { "type": "string" },
            "book_price": { "type": "number" },
            "book_description": { "type": "string" }
        }
    }'''

books_page_data = '''{
"page_title" : "Kitaplar Sayfamıza Hoşgeldiniz",
"page_description" : "Size özel seçilmiş kitaplar;",
"page_sponsor" : "Yazılım Proje",
"page_sponsor_twitter" : "https://twitter.com/yazilimproje",
"page_is_active" : true,
"books" :
    [
        {
          "book_id": 1001,
          "book_name": "Çocuklar için Maker Kitaplığı Seti",
          "book_link": "https://www.robotistan.com/cocuklar-icin-maker-kitapligi-seti",
          "book_price": 202.34,
          "book_description" : "Programcı (coder) olmak zorundasın, Hacker olmak zorundasın..."
        },
        {
          "book_id": 1002,
          "book_name": "IlkByte.com ile tanışın !",
          "book_link": "https://www.ilkbyte.com/",
          "book_price": 93.34,
          "book_description" : "Projeniz için ilk byte bizimle başlasın..."
        }
    ]
}'''

books_page_schema = '''{
  "definitions": {},
  "$schema": "http://json-schema.org/draft-07/schema#",
  "$id": "http://example.com/root.json",
  "type": "object",
  "title": "The Root Schema",
  "required": [
    "page_title",
    "page_description",
    "page_sponsor",
    "page_sponsor_twitter",
    "page_is_active",
    "books"
  ],
  "properties": {
    "page_title": {
      "$id": "#/properties/page_title",
      "type": "string",
      "title": "The Page_title Schema",
      "default": "",
      "examples": [
        "Kitaplar Sayfamıza Hoşgeldiniz"
      ],
      "pattern": "^(.*)$"
    },
    "page_description": {
      "$id": "#/properties/page_description",
      "type": "string",
      "title": "The Page_description Schema",
      "default": "",
      "examples": [
        "Size özel seçilmiş kitaplar;"
      ],
      "pattern": "^(.*)$"
    },
    "page_sponsor": {
      "$id": "#/properties/page_sponsor",
      "type": "string",
      "title": "The Page_sponsor Schema",
      "default": "",
      "examples": [
        "Yazılım Proje"
      ],
      "pattern": "^(.*)$"
    },
    "page_sponsor_twitter": {
      "$id": "#/properties/page_sponsor_twitter",
      "type": "string",
      "title": "The Page_sponsor_twitter Schema",
      "default": "",
      "examples": [
        "https://twitter.com/yazilimproje"
      ],
      "pattern": "^(.*)$"
    },
    "page_is_active": {
      "$id": "#/properties/page_is_active",
      "type": "boolean",
      "title": "The Page_is_active Schema",
      "default": false,
      "examples": [
        true
      ]
    },
    "books": {
      "$id": "#/properties/books",
      "type": "array",
      "title": "The Books Schema",
      "items": {
        "$id": "#/properties/books/items",
        "type": "object",
        "title": "The Items Schema",
        "required": [
          "book_id",
          "book_name",
          "book_link",
          "book_price",
          "book_description"
        ],
        "properties": {
          "book_id": {
            "$id": "#/properties/books/items/properties/book_id",
            "type": "integer",
            "title": "The Book_id Schema",
            "default": 0,
            "examples": [
              1001
            ]
          },
          "book_name": {
            "$id": "#/properties/books/items/properties/book_name",
            "type": "string",
            "title": "The Book_name Schema",
            "default": "",
            "examples": [
              "Çocuklar için Maker Kitaplığı Seti"
            ],
            "pattern": "^(.*)$"
          },
          "book_link": {
            "$id": "#/properties/books/items/properties/book_link",
            "type": "string",
            "title": "The Book_link Schema",
            "default": "",
            "examples": [
              "https://www.robotistan.com/cocuklar-icin-maker-kitapligi-seti"
            ],
            "pattern": "^(.*)$"
          },
          "book_price": {
            "$id": "#/properties/books/items/properties/book_price",
            "type": "number",
            "title": "The Book_price Schema",
            "default": 0.0,
            "examples": [
              202.34
            ]
          },
          "book_description": {
            "$id": "#/properties/books/items/properties/book_description",
            "type": "string",
            "title": "The Book_description Schema",
            "default": "",
            "examples": [
              "Programcı (coder) olmak zorundasın, Hacker olmak zorundasın..."
            ],
            "pattern": "^(.*)$"
          }
        }
      }
    }
  }
}'''


class InfoJson(object):
    # noinspection PyMethodMayBeStatic
    def on_get(self, req, resp, which_is=''):
        print(req)
        print(which_is)
        if which_is == '':
            resp.body = book_data
        elif which_is == 'book-schema':
            resp.body = book_schema
        elif which_is == 'books-page-data':
            resp.body = books_page_data
        elif which_is == 'books-page-schema':
            resp.body = books_page_schema
