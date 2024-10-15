from typing import Dict


def convert2swift(json: Dict[str, str]):
    variable_declaration = ""
    coding_keys = ""
    init_decoder = ""
    init = ""

    for key, value in json.items():
        variable_name = key
        variable_declaration += f"    let {variable_name}: String\n"
        coding_keys += f"        case {variable_name} = \"{key}\"\n"
        init_decoder += f"        self.{variable_name} = try container.decodeIfPresent(String.self, forKey: .{variable_name}) ?? \"{value}\"\n"
        init += f"        {variable_name} = \"{value}\"\n"

    output = f"""
struct Label : Codable {{
{variable_declaration}

    enum CodingKeys : String, CodingKey {{
{coding_keys}
    }}
    
    init(from decoder: Decoder) throws {{
        let container = try decoder.container(keyedBy: CodingKeys.self)
{init_decoder}
    }}
    
    init() {{
{init}
    }}
}}
"""
    return output
