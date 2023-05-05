import sys
import scipdf
from pprint import pprint

article_dict = scipdf.parse_pdf_to_dict(sys.argv[1])

pprint(article_dict)

with open(sys.argv[2], 'w') as f:
    for article in article_dict['sections']:
        print(article["heading"])
        print(article["text"])

        f.write("# ")
        f.write(article["heading"])
        f.write("\n")
        f.write(article["text"])
        f.write("\n")
        f.write("\n")
