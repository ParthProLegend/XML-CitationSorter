import xml.etree.ElementTree as ET

def reverse_xml_sources(input_file, output_file, citation_style):

    if citation_style == "APA":
    
    # Register the namespace prefix 'b' so the output file includes it.
      try:
        ET.register_namespace('b', 'http://schemas.openxmlformats.org/officeDocument/2006/bibliography')
      except AttributeError:
        print("Warning: Could not register namespace. Output XML may lack 'b:' prefix.")

      try:
        tree = ET.parse(input_file)
        root = tree.getroot()

        # Defined namespace to find elements
        namespaces = {'b': 'http://schemas.openxmlformats.org/officeDocument/2006/bibliography'}

        # Finding all <b:Source> elements
        sources = root.findall('b:Source', namespaces)
        
        if not sources:
            print(f"No <b:Source> elements found in {input_file}.")
            return

        print(f"Found {len(sources)} citation sources. Reversing order...")

        # Removing all existing <b:Source> elements from the root
        for source in sources:
            root.remove(source)
            
        sources.reverse()
        
        # Appending  sources back to the root in the new (reversed) order
        for source in sources:
            root.append(source)

        # Write the modified tree to the new output file
        tree.write(output_file, encoding='UTF-8', xml_declaration=True)
        
        print(f"Successfully created {output_file} with reversed citations.")

      except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
      except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
      except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    input_filename = "export.xml"
    output_filename = "export_reversed.xml"
    style = "APA" # American Psychological Association 7th edition
    reverse_xml_sources(input_filename, output_filename, citation_style)
