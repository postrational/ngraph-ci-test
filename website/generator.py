import json

from datetime import datetime
from jinja2 import Environment, PackageLoader, select_autoescape


def _load_trend(path):
    dummy_trend =  [{
    "date": datetime.now().strftime("%m/%d/%Y %H:%M:%S"),
    "failed": 1,
    "passed": 1,
    "skipped": 1
    }]

    try:
        with open(path, "r") as trend_file:
                trend = json.load(trend_file)
    except (IOError, json.decoder.JSONDecodeError):
        trend = dummy_trend
    return trend


ngraph_trend =  [{
    "date": "08/06/2019 09:49:34",
    "failed": 105,
    "passed": 453,
    "skipped": 0
}]




onnxruntime_trend = _load_trend("../results/onnx-runtime/stable/trend.json")
print(onnxruntime_trend)

tensorflow_trend =  [{"date": "08/06/2019 07:29:55", "failed": 64, "passed": 494, "skipped": 0}, {"date": "08/06/2019 08:00:11", "failed": 64, "passed": 494, "skipped": 0}]
pytorch_trend =  [{"date": "08/06/2019 06:51:40", "failed": 151, "passed": 407, "skipped": 0}]


# Coverage percentages
ngraph_coverage = {"total": (ngraph_trend[-1].get("failed", 0) + ngraph_trend[-1].get("passed", 0) + ngraph_trend[-1].get("skipped", 0))}
ngraph_coverage["passed"] = ngraph_trend[-1].get("passed", 0) / ngraph_coverage.get("total", 1) * 100
ngraph_coverage["failed"] = ngraph_trend[-1].get("failed", 0) / ngraph_coverage.get("total", 1) * 100

onnxruntime_coverage = {"total": (onnxruntime_trend[-1].get("failed", 0) + onnxruntime_trend[-1].get("passed", 0) + onnxruntime_trend[-1].get("skipped", 0))}
onnxruntime_coverage["passed"] = onnxruntime_trend[-1].get("passed", 0) / onnxruntime_coverage.get("total", 1) * 100
onnxruntime_coverage["failed"] = onnxruntime_trend[-1].get("failed", 0) / onnxruntime_coverage.get("total", 1) * 100

tensorflow_coverage = {"total": (tensorflow_trend[-1].get("failed", 0) + tensorflow_trend[-1].get("passed", 0) + tensorflow_trend[-1].get("skipped", 0))}
tensorflow_coverage["passed"] = tensorflow_trend[-1].get("passed", 0) / tensorflow_coverage.get("total", 1) * 100
tensorflow_coverage["failed"] = tensorflow_trend[-1].get("failed", 0) / tensorflow_coverage.get("total", 1) * 100

pytorch_coverage = {"total": (pytorch_trend[-1].get("failed", 0) + pytorch_trend[-1].get("passed", 0) + pytorch_trend[-1].get("skipped", 0))}
pytorch_coverage["passed"] = pytorch_trend[-1].get("passed", 0) / pytorch_coverage.get("total", 1) * 100
pytorch_coverage["failed"] = pytorch_trend[-1].get("failed", 0) / pytorch_coverage.get("total", 1) * 100


env = Environment(
    loader=PackageLoader('templates-module', 'templates'),
    autoescape=select_autoescape(['html'])
)

scoreboard_data = {"onnxruntime":{"trend": onnxruntime_trend, "coverage":  onnxruntime_coverage}, \
    "ngraph": {"trend": ngraph_trend, "coverage":  ngraph_coverage},
    "tensorflow": {"trend": tensorflow_trend, "coverage":  tensorflow_coverage},
    "pytorch": {"trend": pytorch_trend, "coverage":  pytorch_coverage}}

index_template = env.get_template('index.html')
index_static = index_template.render(scoreboard_data)

with open("../index.html", "w") as f:
    f.write(index_static)
