def isAnagram(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s.lower()
        t.lower()
        return sorted(s) == sorted(t)

def main():
      s = "racecar"
      t = "carrace"
      print(isAnagram(s, t))
      s = "jar"
      t = "jam"
      print(isAnagram(s, t))


if __name__ == "__main__":
      main()