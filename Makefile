PREFIX = /usr/local
BASEDIR = .

install: 
	@mkdir $(PREFIX)/share/safeclean
	@cp -p $(BASEDIR)/safeclean/safeclean.py $(PREFIX)/share/safeclean
	@ln -s $(PREFIX)/share/safeclean/safeclean.py $(PREFIX)/bin/safeclean

uninstall:
	@rm -f $(PREFIX)/bin/safeclean
	@rm -rf $(PREFIX)/share/safeclean

.PHONY: install uninstall
