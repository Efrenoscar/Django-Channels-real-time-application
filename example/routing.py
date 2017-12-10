from channels.routing import route

channel_routing = [
    route("http.request", "jobs.consumers.http_consumers"),
]
