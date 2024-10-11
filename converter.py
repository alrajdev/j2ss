from typing import Dict


def convert2swift(json: Dict[str, str]):
    output = "struct Label : Codable {\n"
    for key in json.keys():
        output += f"    let {key}: String\n"
    
    output += "\n\n"
    output += "    enum CodingKeys : String, CodingKey {\n"
    for key in json.keys():
        output += f"        case {key} = \"{key}\"\n"
    output += "    }"
    output += "\n\n"

    output += "    init(from decoder: Decoder) throws {\n"
    output += "        let container = try decoder.container(keyedBy: CodingKeys.self)\n"
    for key, value in json.items():
        output += f"        self.{key} = try container.decodeIfPresent(String.self, forKey: .{key}) ?? \"{value}\"\n"
    output += "    }"
    output += "\n\n"

    output += "    init() {\n"
    for key, value in json.items():
        output += f"        {key} = \"{value}\"\n"
    output += "    }\n"
    output += "}\n"

    return output
