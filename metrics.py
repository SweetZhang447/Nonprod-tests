def parse_ratio(numerator, denominator):
  return numerator / denominator


def summarize(values):
  total = 0
  for v in values:
    total += v
  return parse_ratio(total, len(values))
