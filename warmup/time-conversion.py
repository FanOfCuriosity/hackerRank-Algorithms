def timeConversion(s):
    if s[-2:] == 'AM':
        if s[:2] == '12':
            return f"00:{s[3:5]}:{s[6:8]}"
        
        return s[:8]
    
    else:
        if s[:2] == '12':
            return f"00:{s[3:5]}:{s[6:8]}"

        return f"{int(s[:2]) + 12}:{s[3:5]}:{s[6:8]}"
print(timeConversion('07:05:45PM'))
