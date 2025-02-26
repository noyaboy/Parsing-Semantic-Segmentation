import ast
from pprint import pprint

# read data
fp = 'classes_lpcv25.txt'
fp2 = 'imagenet1000_clsidx_to_labels.txt'

with open(fp, 'r', encoding='utf-16') as f:
    lines = f.read()
classes_lpcv = lines.split('\n')[:-1]

with open(fp2, 'r', encoding='utf-8') as f:
    lines = f.read()
classes_in1k_id_label = ast.literal_eval(lines)


# store list of ids and
classes_id_lpcv_to_in1k = []

for i, class_name_lpcv in enumerate(classes_lpcv):
    # empty list to hold the matching ids from imagenet1k
    classes_id_lpcv_to_in1k.append({
        'class_id_lpcv': i, 'class_name_lpcv': class_name_lpcv,
        'matches_in1k': []
    })

    for class_id_in1k, class_name_in1k in classes_in1k_id_label.items():

        # to do:
        # use llmapi to check if the class matches based on definition rather than a string check

        # check if the class from coco is within the imagenet string
        if class_name_lpcv.lower() in class_name_in1k.lower():
            # if it is then add to list
            classes_id_lpcv_to_in1k[i]['matches_in1k'].append({
                'class_id_in1k': class_id_in1k,
                'class_name_in1k': class_name_in1k,    
            })
            # print(class_name_lpcv, class_name_in1k, i, class_id_in1k)

pprint(classes_id_lpcv_to_in1k)

