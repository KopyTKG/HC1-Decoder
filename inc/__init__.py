import json

def annotate(data,schema,File, level=0):
        # load Schema for output
        sch = open("./inc/Schema.json", "r")
        # parse to json
        glb_schema = json.load(sch)

        for key, value in data.items():
            description = schema[key].get('title') or schema[key].get('description') or key
            description, _, _ = description.partition(' - ')
            if type(value) is dict:
                File.write('  '*level + description + "\n")
                _, _, sch_ref = schema[key]['$ref'].rpartition('/')
                annotate(value, glb_schema['$defs'][sch_ref]['properties'], File, level+1)
            elif type(value) is list:
                File.write('  '*level + description + "\n")
                _, _, sch_ref = schema[key]['items']['$ref'].rpartition('/')
                for v in value:
                    annotate(v, glb_schema['$defs'][sch_ref]['properties'], File, level+1)
            else:
                File.write('  '*level + description + ':' + str(value) + "\n")