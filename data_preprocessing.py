def read_documents():
    f = open("INSERT PATH") # file is accessed locally
    merged = ""

    for a_line in f.readlines():
        if a_line.startswith("."):
            merged += "\n" + a_line.strip()
        else:
            merged += " " + a_line.strip()

    documents = {}

    content = ""
    doc_id = ""

    for a_line in merged.split("\n"):
        if a_line.startswith(".I"):
            doc_id = a_line.split(" ")[1].strip()
        elif a_line.startswith(".X"):
            documents[doc_id] = content
            content = ""
            doc_id = ""
        else:
            content += a_line.strip()[3:] + " "
    f.close()
    return documents

documents = read_documents()
print(f"{len(documents)} documents in total")
print("Document with id 1:")
print(documents.get("1"))

def read_queries():
    #f = open("cisi/CISI.QRY") # same as above; use a different command if running in Colab
    f = open("/content/drive/MyDrive/" + "Colab Notebooks/" + "cisi/CISI.QRY") #if via Colab
    merged = ""

    for a_line in f.readlines():
        if a_line.startswith("."):
            merged += "\n" + a_line.strip()
        else:
            merged += " " + a_line.strip()

    queries = {}

    content = ""
    qry_id = ""

    for a_line in merged.split("\n"):
        if a_line.startswith(".I"):
            if not content=="":
                queries[qry_id] = content
                content = ""
                qry_id = ""
            qry_id = a_line.split(" ")[1].strip()
        elif a_line.startswith(".W") or a_line.startswith(".T"):
            content += a_line.strip()[3:] + " "
    queries[qry_id] = content
    f.close()
    return queries

queries = read_queries()
print(f"{len(queries)} queries in total")
print("Query with id 1:")
print(queries.get("1"))

def read_mappings():
    #f = open("cisi/CISI.REL") # different command if running in Colab; see above
    f = open("/content/drive/MyDrive/" + "Colab Notebooks/" + "cisi/CISI.REL") #if via Colab

    mappings = {}

    for a_line in f.readlines():
        voc = a_line.strip().split()
        key = voc[0].strip()
        current_value = voc[1].strip()
        value = []
        if key in mappings.keys():
            value = mappings.get(key)
        value.append(current_value)
        mappings[key] = value

    f.close()
    return mappings

mappings = read_mappings()
print(f"{len(mappings)} mappings in total")
print(mappings.keys())
print("Mapping for query with id 1:")
print(mappings.get("1"))