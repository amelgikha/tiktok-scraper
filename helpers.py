def process_results(data):
    nested_values = ['video', 'author', 'music', 'stats', 'authorStats', 'challenges', 'duetInfo', 'textExtra', 'stickersOnItem']
    skip_values = ['challenges', 'duetInfo', 'textExtra', 'stickersOnItem']


    flattened_data = {}

    for idx, value in enumerate(data):
        flattened_data[idx] = {}

        for prop_idx, prop_value in value.items():

            if prop_idx in nested_values:
                if prop_idx in skip_values:
                    pass
                else:
                    for nested_idx, nested_value in prop_value.items():
                        flattened_data[idx][prop_idx+'_'+nested_idx] = nested_value

            else:
                flattened_data[idx][prop_idx] = prop_value

    return flattened_data