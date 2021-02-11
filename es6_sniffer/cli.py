import json
import glob
import os
import pprint

import click
import semantic_version


def get_formatted_node_version(engines):
    if isinstance(engines, dict) and engines.get('node'):
        if isinstance(engines['node'], list):
            node_version = ','.join(engines['node'])

        elif isinstance(engines['node'], str):
            node_version = engines['node']

        else:
            raise ValueError('Unexpected value for target Node versions: {}'.format(engines['node']))

    elif isinstance(engines, list):
        node_version = ','.join([e.replace('node', '') for e in engines if 'node' in e])

    else:
        node_version = ''

    formatted_node_version = node_version.replace(' ', '')\
                                         .replace('x', '0')\
                                         .replace('^', '>=')\
                                         .replace('||', ',')

    return formatted_node_version or None


@click.command()
@click.option('--include-unspecified', '-i', is_flag=True, default=False, help='Include packages where engine is unspecified.')
@click.option('--node-modules', default='node_modules', required=False, help='Relative path to node_modules/')
def main(node_modules, include_unspecified):
    '''
    Node ES6 matrix: https://node.green/#ES2016
    '''
    n_packages = 0
    n_engines = 0
    n_no_engines = 0

    to_transpile = []

    for package_config in glob.glob(os.path.join(node_modules, '*', 'package.json')):
        n_packages += 1

        with open(package_config, 'r') as f:
            package = json.load(f)

        try:
            engines = package['engines']

        except KeyError:
            n_no_engines += 1

            if include_unspecified:
                to_transpile.append(package_config)

        except:
            continue

        else:
            print('{0}: {1}'.format(package_config, engines))

            max_node_version = semantic_version.Version('0.12.18')

            package_node_version = get_formatted_node_version(engines)

            if max_node_version in semantic_version.SimpleSpec(package_node_version):
                print('{} includes max version'.format(package_config))

            else:
                print('{} exceeds max version'.format(package_config))
                to_transpile.append(package_config)

            n_engines += 1

    print('Found {0} packages, {1} with engines, {2} without engines'.format(n_packages, n_engines, n_no_engines))
    print('Recommend transpiling {} packages'.format(len(to_transpile)))
    pprint.pprint([os.path.dirname(package) for package in to_transpile])
