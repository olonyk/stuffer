import xml.etree.ElementTree as ET

from pkg_resources import resource_filename, resource_listdir, resource_string


class DataHandler():
    def __init__(self):
        self.root = None
        self.read_data()
    
    def read_data(self):
        tree = ET.parse(resource_filename("resources.data", "data.xml"))
        self.root = tree.getroot()
    
    def get_topics(self):
        topics = []
        for topic in self.root:
            topics.append(topic.attrib["name"])
        return topics

    def get_attrib(self, topics):
        attrib = {}
        for topic in self.root.findall('topic'):
            if topic.get("name") in topics:
                elements = []
                for item in topic.findall("item"):
                    elements += [t.tag for t in list(item)]
                attrib[topic.get("name")] = list(set(elements))
                attrib[topic.get("name")].remove("stats")
        return attrib
