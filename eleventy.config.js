import { govukEleventyPlugin } from '@x-govuk/govuk-eleventy-plugin';
import * as esbuild from 'esbuild'
import * as fs from 'fs';
import * as path from 'path';

export default function(eleventyConfig) {
  eleventyConfig.addBundle("js", {
    toFileDirectory: "bundle",
    outputFileExtension: "js",
    shortcodeName: "js",
    transforms: [
      async function(code) {
        async function copyDir(src, dest) {
            let entries = fs.readdirSync(src, { recursive: true, withFileTypes: true })

            for (let entry of entries) {
                let srcPath = path.join(entry.parentPath, entry.name);
                let destPath = srcPath.replace(src, dest);
                let destDir = path.dirname(destPath);

                if (entry.isFile()) {
                  fs.mkdirSync(destDir, { recursive: true })
                  fs.copyFileSync(srcPath, destPath);
                }
            }
        }

        await copyDir('_includes/javascripts', 'tmp')

        const app = fs.readFileSync('./tmp/application.mjs')
        
        fs.writeFileSync('./tmp/index.mjs', app + "\n" + code)
        
        esbuild.buildSync({
          entryPoints: ['./tmp/index.mjs'],
          outfile: './tmp/out.js',
          minify: process.env.ELEVENTY_RUN_MODE == 'build',
          bundle: true,
        })
        return fs.readFileSync('./tmp/out.js', 'utf8')
      }
    ],
    hoist: true,
    bundleExportKey: "bundle",
  });

  // Register the plugin
  eleventyConfig.addPlugin(govukEleventyPlugin, {
    homeKey: 'Home',
    titleSuffix: 'GOV.UH content and publishing guidance',
    showBreadcrumbs: true,
    stylesheets: [
      '/assets/styles.css'
    ],
    header: {
      productName: 'Content and publishing guidance',
      search: {
        indexPath: '/search.json',
        sitemapPath: '/sitemap',
        label: "Search guidance"
      }
    },
    serviceNavigation: {
      navigation: [
        {
            text: "Writing standards",
            href: "/writing-to-gov-uk-standards"
        },
        {
          text: "Publishing content",
          href: "/publish-update-retire-content"
        },
        {   
          text: "Formatting content",
          href: "/formatting-content"
        },
         {
	        text: "Accounts and support",
	        href: "/accounts-support"
      },
        {
          text: "National events",
          href: "/publishing-national-events"  
        },
     
      ]

    },
    footer: {
      meta: {
        items: [
          {
            href: "/accessibility-statement",
            text: "Accessibility statement"
          },
          {
            href: "/sitemap",
            text: "Sitemap"
          },
          {
            href: "/cookies",
            text: "Cookies"
          },
          {
            href: "/privacy-notice",
            text: "Privacy notice"
          },
          {
            href: "/about-the-guidance/whats-new",
            text: "What's new"
          },
        ],
        html: '<a href="https://www.gov.uhrblx.com/" class="govuk-footer__link">GOV.UH</a>.',
      }
    },
    templates: {
      searchIndex: false,
    }
  });
  eleventyConfig.addPreprocessor("macro-inject", ".njk,.md", (data, content) => {
		return `{%- from "call-to-action.njk" import cta with context -%}\n` + content;
	});


  return {
    dataTemplateEngine: 'njk',
    htmlTemplateEngine: 'njk',
    markdownTemplateEngine: 'njk',
    dir: {
      // The folder where all your content will live:
      input: 'app',
      // Use layouts from the plugin
      includes: '../_includes',
      layouts: '../_includes/layouts'
    },
    serverOptions: {
      port: process.env.PORT || 8080
    }
  }
};
