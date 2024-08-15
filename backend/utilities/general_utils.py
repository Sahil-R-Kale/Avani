def replace_dict_keys(original_dict):
    key_mapping = {
    'ans_q4_processed': 'Land size used for Onion',
    'ans_q5_processed': 'Last Soil Testing',
    'ans_q6_processed': 'Quantity of seeds sown',
    'ans_q7_processed': 'Water source/s for the farm',
    'ans_q8_processed': 'Availability of water in the last season',
    'ans_q9_processed': 'Availability of Electricity in the last season',
    'ans_q10_processed': 'Availability of Labour in the last season',
    'ans_q13_processed': 'Production estimate for this season',
    'ans_q14_processed': 'Storage conditions',
    'farmer_name': "Farmer Name",
    'taluka':"Taluka",
    'village':"Village"
    }

    new_dict = {key_mapping.get(k, k): v for k, v in original_dict.items()}
    return new_dict

def add_bivariate_text(data):
    data += ["The correlation between the area of onion farm and the quantity of onion seeds planted is 0.84. Greater is Area of onion farm, greater will be Quantity of onion seeds planted.",
    "The correlation between water availability and the area of onion farm is -0.94. Lower is Area of onion farm, greater will be Water availability.",
    "The correlation between electricity availability and the area of onion farm is -0.81. Lower is Area of onion farm, greater will be Electricity availability.",
    "The correlation between labour availability and the area of onion farm is -0.72. Lower is Area of onion farm, greater will be Labour availability.",
    "The correlation between the ratio of seeds sown to land size and the area of onion farm is 0.42. The correlation is moderate and positive. Greater is area of onion farm, more is the ratio of seeds sown to land size.",
    "As p-value&gt;0.05, there is no significant difference in the mean 'Area of onion farm' across different categories of 'Water availability'.",
    "From a Chi-square test, the P-value&lt; 0.05, there is a significant association between 'Labour availability' and 'Water availability'."
    ]
    return data

def add_univariate_text(data):
    data += ["100.00% of farmers have planted onion",
    "Average area of onion planted: 5.79 acres",
    "Average area of onion planted: 5.79 acres",
    "Minimum area of onion planted: 2.50 acres",
    "Maximum area of onion planted: 10.00 acres",
    "62.50% of farmers have carried out a soil test in the last 5 years",
    "37.50% of farmers have never carried out a soil test or have carried out a soil test more than 5 years ago",
    "Water Availability was very Problematic for majority(62.50%) of farmers",
    "Electricity Availability was manageable/no problems for majority (37.50% each) of farmers",
    "Electricity Availability was problematic or very problematic for only 25.00%  of farmers",
    "Labour Availability was problematic or very problematic for 37.50% of farmers",
    "Labour Availability was manageable for majority (37.50%) of farmers",
    "Number of unique talukas: 3",
    "Most common taluka: Yeola with 6 occurrences",
    "Number of unique villages: 7",
    "Most common village: Nagade with 2 occurrences",
    "46.15% of farmers use well water which is the maximum.",
    "23.08% of farmers use canal water",
    ]
    return data
