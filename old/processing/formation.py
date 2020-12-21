def get_formatted_data(dataset, clusters):
    out = dict(zip(dataset, clusters.labels_.tolist()))

    new_out = {}
    for key, value in out.items():
        if value not in new_out:
            new_out[value] = [key]
        else:
            new_out[value].append(key)

    return {k: v for k, v in sorted(new_out.items(), key=lambda item: len(item[1]), reverse=True)}


def get_values(formatted_data):
    return list(formatted_data.values())[1:]


if __name__ == '__main__':
    pass
