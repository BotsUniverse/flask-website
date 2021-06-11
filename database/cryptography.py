class Crypto:
    def __init__(self, text: str, key: str):
        """[Converts the text into some hashed number or vice versa.]

        :param text: [The text to be hashed.]
        :type text: str
        :param key: [The key to hash the text with.]
        :type key: str
        """
        self.txt = text
        self.key = key



    def encode(self):
        try:
            splt_txt = [ord(char) for char in self.txt] if self.txt else []
            splt_key = [ord(char) for char in self.key] if self.key else []

            total = ""

            for index in range(len(splt_txt)):
                added = splt_txt[index] + splt_key[(index % (len(splt_key)-1))]
                total += str(added) + " "

            return {
                "key": self.key,
                "encoded": total.strip(),
                "decoded": self.txt,
                "result": total.strip(),
                "error": None
            }

        except Exception as e:
            return {
                "key": self.key,
                "encoded": total,
                "decoded": self.txt,
                "result": total.strip(),
                "error": None
            }




    def decode(self):
        total = ""

        try:
            

            splt_txt = [int(item) for item in self.txt.split()]
            splt_key = [ord(char) for char in self.key]


            for index in range(len(splt_txt)):
              sub_num = splt_txt[index] - splt_key[index % (len(splt_key)-1)]
              total += chr(sub_num)
            
            return {
                "key": self.key,
                "encode": self.txt,
                "decode": total,
                "result": total,
                "error": None
            }


        except Exception as e:
            return {
                "key": self.key,
                "encode": self.txt,
                "decode": total,
                "result": total,
                "error": e
            }