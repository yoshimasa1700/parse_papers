import sys
import scipdf
from pprint import pprint

article_dict = scipdf.parse_pdf_to_dict(sys.argv[1])

pprint(article_dict)



def nl(f):
    f.write("\n")


def header(f, text, depth=0):
    mark = "#" * (depth+1) + ' '
    f.write(mark + text)
    nl(f)
    nl(f)


with open(sys.argv[2], 'w') as f:
    # write title
    header(f, article_dict['title'])

    # write paper info
    header(f, "info", 1)

    header(f, "authors", 2)
    f.write(article_dict["authors"])
    nl(f)
    nl(f)

    header(f, "pub_date", 2)
    f.write(article_dict["pub_date"])
    nl(f)
    nl(f)

    # write abstract
    header(f, "abstract", 1)
    f.write(article_dict["abstract"])
    nl(f)
    nl(f)

    # write article
    header(f, "article", 1)

    for article in article_dict['sections']:
        header(f, article["heading"], 2)
        f.write(article["text"])

        nl(f)
        nl(f)

    header(f, 'references', 2)
    # write refs
    for idx, ref in enumerate(article_dict['references']):
        f.write('[{}] '.format(idx+1))
        f.write(ref['authors'])
        f.write(', ')
        f.write(ref['title'])
        f.write(', ')
        f.write(ref['journal'])
        f.write(', ')
        f.write(ref['year'])

        nl(f)
