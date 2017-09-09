from collections import OrderedDict, Mapping
import json

COMPACT_SEPARATORS = (',', ':')

def order_by_key(kv):
  return kv[0]

def recursive_order(node):
  if isinstance(node, Mapping):
    ordered_mapping = OrderedDict(sorted(node.items(), key=order_by_key))
    for key, value in ordered_mapping.items():
      ordered_mapping[key] = recursive_order(value)
    return ordered_mapping
  return node

def stringify(node):
  return json.dumps(recursive_order(node), separators=COMPACT_SEPARATORS)

__all__ = ['stringify']
