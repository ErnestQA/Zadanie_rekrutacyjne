### 1. Jakie znasz lokalizatory w Selenium? Których najczęściej używasz i dlaczego?
**Odpowiedź:** Znam lokalizatory: `id`, `name`, `className`, `css selector`, `xpath`, `tag name`, `link text`.  
Chciałbym używać `id`, ponieważ jest krótki i niezawodny, ale nie wszystkie elementy mają `id`, dlatego w praktyce częściej korzystam z `xpath`.
### 2. Czym różni się findElement() od findElements() w Selenium WebDriver?
**Odpowiedź:** findElement() szuka jednego elementu i zwraca go; rzuca wyjątek, jeśli element nie istnieje.
findElements() szuka elementy i zwraca listę; jeśli nic nie znajdzie, zwraca pustą listę.
### 3. Jak poradziłbyś sobie z elementem, który ładuje się dynamicznie (np. Ajax)?
**Odpowiedź:** Kiedy trafiam na element, który ładuje się dynamicznie, wykorzystuję Explicit Wait i sprawdzam warunki za pomocą Expected Conditions.
### 4. Jakie masz doświadczenie z używaniem Explicit Wait i Implicit Wait?
**Odpowiedź:** Oczywiście. Emplicit Wait wykorzestuję dla poszukiewannia elementów i sprawdzania ich stanu za pomocy Expected Conditions. Implicit Wait stosuje do drivera żeby ustalić czas, za którzy driver będzie probowaw dopokać się do elementu. driver.implicitly_wait(10)
### 5. Jak radzisz sobie z testowaniem elementów w iframe?
**Odpowiedź:** Nie lubię ich, ale radzę sobie. Trzeba pamiętać, żeby przełączyć się do iframe i później wrócić do głównego dokumentu. 
driver.switch_to.frame("")
driver.switch_to.default_content()
### 6. Jakie masz podejście do obsługi okien popup/modalnych w Selenium?
**Odpowiedź:** Trzeba czekać stanu pewnego ladowania za pomogo Explicit Wait + Expected Conditions
### 7.Czy integrowałeś Selenium z innymi narzędziami (np. Jenkins, Allure, JUnit, TestNG, Cucumber)?
**Odpowiedź:** Tak, z Jenkins ta Allure
### 8. Opowiedz o trudnym błędzie, jaki napotkałeś podczas testowania automatycznego i jak go rozwiązałeś.
**Odpowiedź:** Miałem sytuację, kiedy nie mogłem znaleźć lokatora, bo web element pojawiał się tylko przy skierowaniu kursora na niego, a kiedy klikałem prawą przyciskiem myszy, element znikał. Musiałem użyć kodu JS do uruchomienia debuggera, co pozwoliło mi "zamrozić" element, kiedy się pojawił.
### 9. Co robisz, gdy test losowo przechodzi lub się nie powodzi (flaky test)?
**Odpowiedź:** Najpierw sprawdzam najbardziej prawdopodobne miejsca: lokatory, timingi, zależności zewnętrzne.
Jeżeli to nie pomaga, próbuję zamockować lub dodać ponowne uruchamianie testów.
Jeżeli nadal nie pomaga, a czas nagli, tymczasowo odkładam te flaky-testy i kontynuuję z tym, co działa.
### 10. Jakie techniki stosujesz, aby utrzymać testy automatyczne w dobrej kondycji w czasie?
**Odpowiedź:** Wykorzystuję Explicit Wait i niezawodne lokatory z użyciu XPath.
### 11. Wyobraź sobie, że po deployu przestały działać wszystkie testy. Jak przystępujesz do diagnozy problemu?
**Odpowiedź:** Najpierw sprawdzam i analizuję logi testów, analizuję zminy w kodzie, spawdzam lokatory i timingy. Aktualizuję testy 
### 12. W jakim języku programujesz testy (Java, Python, C#)? Dlaczego akurat ten język?
**Odpowiedź:** Python — używam go, bo jest wygodny i dobrze nadaje się do automatyzacji testów. Jest dobrze zegrany z Selenium. 
### 13. Jakie masz doświadczenie z GIT i pracą z repozytorium kodu?
**Odpowiedź:** Urzywal git, ale nie dlugo. mam raczej podstawowę wiedzie. ale szybko się uczę i jestem pewien, że nadrobię ten temat.
### 14. Czy stosowałeś testy równoległe (parallel execution)? Jak je konfigurowałeś?
**Odpowiedź:** Osobiście nie stosowałem, ale wiem, że jest to możliwe z użyciem Pytest.
### 15. Czy masz doświadczenie z CI/CD? Jak wyglądał proces uruchamiania testów automatycznych w Twoim zespole?
**Odpowiedź:** Odpalaliśmy testy po odświeżeniu produktu przez Jenkins.
### 16. Kiedy nie warto automatyzować testu?
**Odpowiedź:** Kiedy testy nie wykonują się wielokrotnie, kiedy testy nie są niestabilne.
### 17.Jak określasz, które testy warto automatyzować?
**Odpowiedź:** Automatyzuję testy, które często się powtarzają, są stabilne, testy w ramach regresji.
### 18. Jakie są Twoim zdaniem największe wyzwania w testach automatycznych z użyciem Selenium?
**Odpowiedź:** Największe wyzwania w Selenium, z mojego doświadczenia, to niestabilność testów związana z dynamicznie ładującymi się elementami – czasami Selenium nie może znaleźć elementu lub przegapia go.
### 19. Czy miałeś doświadczenie z testowaniem aplikacji mobilnych lub desktopowych?
**Odpowiedź:** Tak, oczywiście, ale generalnie pracowałem z aplikacjami desktopowymi
