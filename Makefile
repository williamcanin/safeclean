PREFIX ?= /usr/local

install: bin/safeclean
	@cp -p $< $(PREFIX)/$<

uninstall:
	rm -f $(PREFIX)/bin/safeclean

.PHONY: install uninstall
