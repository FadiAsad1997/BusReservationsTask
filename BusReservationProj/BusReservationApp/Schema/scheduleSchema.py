schedule_schema = {
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "required": True
        },
        "busID": {
            "type": "number",
            "minimum": 1,
            "required": True
        },

        "srcTimeStamp": {
            "type": "number",
            "minimum": 1,
            "required": True
        },
        "srcStationID": {
            "type": "number",
            "minimum": 1,
            "required": True
        },
        "dstStationID": {
            "type": "number",
            "minimum": 1,
            "required": True
        },
        "isAvailable": {
            "type": "number",
            "minimum": 0,
            "maximum": 1,
            "required": True
        },
    }
}
